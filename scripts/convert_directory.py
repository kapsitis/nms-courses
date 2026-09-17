#!/usr/bin/env python3
"""Batch-convert the Markdown files of a course directory to .docx and .pdf.

For every subdirectory directly under ``input_dir``, each ``*.md`` file in it
that has ``docx_*`` front-matter is converted with md_to_docx.convert() and, via
pandoc + the Eisvogel LaTeX template, to a PDF of the same name. Files without
such front-matter (index.md, README.md, ...) are skipped.

The .docx is written next to its source under a download-friendly name that
encodes the file's path relative to the GitHub Pages root (the nearest ancestor
directory holding ``_config.yml``), joined with '-'. Two-digit school-year
components such as ``26_27`` are expanded to ``2026_27``:

    docs/matf78/26_27/78STRUCT_solution_structure/problems.md
      -> docs/matf78/26_27/78STRUCT_solution_structure/
         matf78-2026_27-78STRUCT_solution_structure-problems.docx

Existing .docx/.pdf files are overwritten.

The PDF reuses the front-matter: ``geometry`` is read by pandoc itself, while
``docx_header``/``docx_header_right``/``docx_footer`` become Eisvogel's running
header and footer, and ``docx_fontsize`` its base size. ``::: solution`` blocks
are kept (as in the .docx) by online-tests/solutions.lua.

Requires, on top of md_to_docx's needs: the Eisvogel pandoc template and a
LaTeX installation providing lualatex.

Usage:
    python scripts/convert_directory.py <input_dir>
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from md_to_docx import (convert, has_docx_front_matter, normalize_footer,
                        parse_front_matter, translate_image_sizes)

_SCHOOL_YEAR = re.compile(r"^\d{2}_\d{2}$")
# The same reader extensions the repo's other PDF scripts use.
_PANDOC_FROM = "markdown+tex_math_dollars+pipe_tables"
_REPO_ROOT = Path(__file__).resolve().parent.parent
# Preamble fix for Eisvogel + pandoc >= 3.2 tables.
_PDF_HEADER = Path(__file__).resolve().parent / "pdf_header.tex"


def site_root(path: Path) -> Path | None:
    """Return ``path`` or its nearest ancestor containing Jekyll's _config.yml."""
    path = path.resolve()
    for parent in (path, *path.parents):
        if (parent / "_config.yml").exists():
            return parent
    return None


def prefixed_name(md_path: Path, root: Path, suffix: str) -> str:
    """Build e.g. 'matf78-2026_27-78STRUCT_solution_structure-problems.docx'."""
    parts = md_path.resolve().relative_to(root).with_suffix("").parts
    parts = [f"20{p}" if _SCHOOL_YEAR.match(p) else p for p in parts]
    return "-".join(parts) + suffix


def find_lua_filter(md_path: Path) -> Path | None:
    """solutions.lua from the Markdown's own folder, else the repo's copy."""
    for candidate in (md_path.parent / "solutions.lua",
                      _REPO_ROOT / "online-tests" / "solutions.lua"):
        if candidate.exists():
            return candidate
    return None


def convert_pdf(md_path: Path, pdf_path: Path, *, show_solutions: bool = True) -> None:
    """Convert ``md_path`` to ``pdf_path`` with pandoc + the Eisvogel template.

    Raises subprocess.CalledProcessError if pandoc (or LaTeX) fails.
    """
    fm = parse_front_matter(md_path)
    # Eisvogel's header/footer slots mirror what md_to_docx puts in the .docx.
    variables = {
        "colorlinks": "true",
        "header-left": fm.get("docx_header", ""),
        "header-right": fm.get("docx_header_right", ""),
        "footer-right": " ".join(normalize_footer(fm.get("docx_footer"))),
        "footer-left": "",
    }
    if fm.get("docx_fontsize"):
        variables["fontsize"] = f"{fm['docx_fontsize']}pt"

    cmd = ["pandoc", "-o", str(pdf_path), "--from", _PANDOC_FROM,
           "--pdf-engine=lualatex", "--template", "eisvogel",
           "--include-in-header", str(_PDF_HEADER),
           f"--resource-path={md_path.parent}",
           # Blank title: no Eisvogel title block, while Jekyll keeps its own.
           "--metadata", "title=",
           "--metadata", f"show-solutions={str(show_solutions).lower()}"]
    for name, value in variables.items():
        cmd += ["-V", f"{name}={value}"]
    lua_filter = find_lua_filter(md_path)
    if lua_filter:
        cmd += [f"--lua-filter={lua_filter}"]

    # Image widths are written as kramdown IALs; pandoc needs its own syntax.
    # The temp file lives beside the source so relative image paths resolve.
    tmp = tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", suffix=".md", dir=str(md_path.parent), delete=False)
    try:
        tmp.write(translate_image_sizes(md_path.read_text(encoding="utf-8")))
        tmp.close()
        cmd.insert(1, tmp.name)
        subprocess.run(cmd, check=True)
    finally:
        Path(tmp.name).unlink(missing_ok=True)
    print(f"Wrote {pdf_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert .md files in the subdirectories of a directory to prefixed .docx files."
    )
    parser.add_argument("input_dir", help="Directory whose subdirectories are scanned, e.g. docs/matf78/26_27/")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    if not input_dir.is_dir():
        sys.exit(f"Not a directory: {input_dir}")
    # Outside a Jekyll site, encode the path starting from input_dir itself.
    root = site_root(input_dir) or input_dir.resolve().parent

    converted, failed = 0, []
    for subdir in sorted(d for d in input_dir.iterdir() if d.is_dir()):
        for md_path in sorted(subdir.glob("*.md")):
            if not has_docx_front_matter(md_path):
                print(f"Skipped {md_path} (no docx_* front-matter)")
                continue
            try:
                convert(md_path, md_path.with_name(prefixed_name(md_path, root, ".docx")))
                converted += 1
            except SystemExit as exc:  # md_to_docx reports errors via sys.exit
                print(f"FAILED (docx) {md_path}: {exc}", file=sys.stderr)
                failed.append(md_path)
            try:
                convert_pdf(md_path, md_path.with_name(prefixed_name(md_path, root, ".pdf")))
                converted += 1
            except (subprocess.CalledProcessError, FileNotFoundError) as exc:
                print(f"FAILED (pdf) {md_path}: {exc}", file=sys.stderr)
                failed.append(md_path)

    print(f"\nWrote {converted} output file(s), {len(failed)} failed.")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
