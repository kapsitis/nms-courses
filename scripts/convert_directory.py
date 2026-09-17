#!/usr/bin/env python3
"""Batch-convert the Markdown files of a course directory to .docx.

For every subdirectory directly under ``input_dir``, each ``*.md`` file in it
that has ``docx_*`` front-matter is converted with md_to_docx.convert(). Files
without such front-matter (index.md, README.md, ...) are skipped.

The .docx is written next to its source under a download-friendly name that
encodes the file's path relative to the GitHub Pages root (the nearest ancestor
directory holding ``_config.yml``), joined with '-'. Two-digit school-year
components such as ``26_27`` are expanded to ``2026_27``:

    docs/matf78/26_27/78STRUCT_solution_structure/problems.md
      -> docs/matf78/26_27/78STRUCT_solution_structure/
         matf78-2026_27-78STRUCT_solution_structure-problems.docx

Existing .docx files are overwritten.

Usage:
    python scripts/convert_directory.py <input_dir>
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from md_to_docx import convert, has_docx_front_matter

_SCHOOL_YEAR = re.compile(r"^\d{2}_\d{2}$")


def site_root(path: Path) -> Path | None:
    """Return ``path`` or its nearest ancestor containing Jekyll's _config.yml."""
    path = path.resolve()
    for parent in (path, *path.parents):
        if (parent / "_config.yml").exists():
            return parent
    return None


def prefixed_docx_name(md_path: Path, root: Path) -> str:
    """Build e.g. 'matf78-2026_27-78STRUCT_solution_structure-problems.docx'."""
    parts = md_path.resolve().relative_to(root).with_suffix("").parts
    parts = [f"20{p}" if _SCHOOL_YEAR.match(p) else p for p in parts]
    return "-".join(parts) + ".docx"


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
            docx_path = md_path.with_name(prefixed_docx_name(md_path, root))
            try:
                convert(md_path, docx_path)
                converted += 1
            except SystemExit as exc:  # md_to_docx reports errors via sys.exit
                print(f"FAILED {md_path}: {exc}", file=sys.stderr)
                failed.append(md_path)

    print(f"\nConverted {converted} file(s), {len(failed)} failed.")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
