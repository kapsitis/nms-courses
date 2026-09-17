#!/usr/bin/env python3
"""Make Jekyll permalinks match file paths and add default .docx front-matter.

Every ``*.md`` file under ``input_dir`` (recursively) that has YAML front-matter
gets a permalink derived from its path relative to the GitHub Pages root (the
nearest ancestor holding ``_config.yml``):

    docs/matf78/26_27/78STRUCT_solution_structure/problems.md
      -> permalink: /matf78/26_27/78STRUCT_solution_structure/problems/
    docs/matf78/26_27/78STRUCT_solution_structure/index.md
      -> permalink: /matf78/26_27/78STRUCT_solution_structure/

Files other than index.md also get the .docx keys used by md_to_docx.py
(docx_header = the first H1 heading; the footer names the grades taken from a
``matfNN`` path component, e.g. matf910 -> "9.-10."). Only MISSING keys are
added; existing values are left untouched. Files without front-matter (e.g.
README.md) are skipped.

The front-matter is edited as text, so key order, quoting and comments stay as
they were. Changed permalinks are listed together with any places in the site
that still refer to the old URL.

Usage:
    python scripts/fix_permalinks.py <input_dir>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from convert_directory import site_root
from md_to_docx import parse_front_matter

_COURSE = re.compile(r"^matf(\d)(\d+)$")   # matf78 -> 7, 8; matf910 -> 9, 10
_H1 = re.compile(r"^#[ \t]+(.+?)[ \t#]*$")
_FENCE = re.compile(r"^(```|~~~)")


def expected_permalink(md_path: Path, root: Path) -> str:
    rel = md_path.resolve().relative_to(root).with_suffix("")
    parts = rel.parts[:-1] if rel.name == "index" else rel.parts
    return "/" + "".join(f"{p}/" for p in parts)


def first_h1(body_lines: list[str]) -> str | None:
    in_fence = False
    for line in body_lines:
        if _FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence and (m := _H1.match(line)):
            return m.group(1)
    return None


def docx_defaults(md_path: Path, header: str) -> dict[str, object]:
    grades = next((f"{m.group(1)}.-{m.group(2)}." for p in md_path.resolve().parts
                   if (m := _COURSE.match(p))), "7.-8.")
    return {
        "docx_header": header,
        "docx_footer": f"ĀVĢ {grades}klašu matemātikas fakultatīvs",
        "docx_font": "Calibri",
        "docx_fontsize": 10,
        "docx_heading_font": "Calibri Light",
        "docx_heading_color": "2F5496",
        "docx_heading1_size": 14,
        "geometry": "a4paper, top=2.54cm, bottom=2.54cm, left=2.54cm, right=2.54cm",
    }


def yaml_value(value: object) -> str:
    # A JSON string is also a valid YAML double-quoted scalar.
    return json.dumps(value, ensure_ascii=False) if isinstance(value, str) else str(value)


def fix_file(md_path: Path, root: Path) -> str | None:
    """Update ``md_path`` in place; return its old permalink if it changed."""
    raw = md_path.read_bytes().decode("utf-8")  # read_text() would turn CRLF into LF
    newline = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.split(newline)
    if not lines or lines[0].strip() != "---":
        print(f"Skipped {md_path} (no front-matter)")
        return None
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        print(f"Skipped {md_path} (unterminated front-matter)")
        return None

    fm = parse_front_matter(md_path)
    head, body = lines[1:end], lines[end + 1:]
    notes = []

    permalink = expected_permalink(md_path, root)
    old = fm.get("permalink")
    if old != permalink:
        new_line = f"permalink: {permalink}"
        idx = next((i for i, l in enumerate(head) if l.startswith("permalink:")), None)
        if idx is not None:
            head[idx] = new_line
        else:
            after = next((i + 1 for i, l in enumerate(head) if l.startswith("title:")), len(head))
            head.insert(after, new_line)
        notes.append(f"permalink {old or '(none)'} -> {permalink}")

    if md_path.name != "index.md":
        header = first_h1(body) or str(fm.get("title", ""))
        missing = {k: v for k, v in docx_defaults(md_path, header).items() if k not in fm}
        if missing:
            while head and not head[-1].strip():
                head.pop()
            if not any(str(k).startswith("docx_") for k in fm):
                head.append("")
            head += [f"{k}: {yaml_value(v)}" for k, v in missing.items()]
            notes.append(f"added {', '.join(missing)}")

    if notes:
        md_path.write_text(newline.join(["---", *head, *lines[end:]]),
                           encoding="utf-8", newline="")
        print(f"Updated {md_path}: " + "; ".join(notes))
    return old if old and old != permalink else None


def report_stale_links(root: Path, changed: dict[str, str]) -> None:
    """List site files that still mention a replaced permalink."""
    for path in sorted(root.rglob("*")):
        if path.suffix not in (".md", ".html", ".yml", ".yaml") or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for old, new in changed.items():
            # Not followed by more path, so "/a/" doesn't match inside "/a/b/".
            if re.search(re.escape(old) + r"(?![\w/.-])", text):
                print(f"  {path}: still links to {old} (now {new})")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Set permalinks from file paths and add missing docx_* front-matter."
    )
    parser.add_argument("input_dir", help="Directory to scan recursively, e.g. docs/matf78/26_27/")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    if not input_dir.is_dir():
        sys.exit(f"Not a directory: {input_dir}")
    root = site_root(input_dir)
    if root is None:
        sys.exit(f"No _config.yml found above {input_dir}; cannot determine the site root.")

    changed = {}
    for md_path in sorted(input_dir.rglob("*.md")):
        old = fix_file(md_path, root)
        if old:
            changed[old] = expected_permalink(md_path, root)

    if changed:
        print("\nReferences to changed permalinks:")
        report_stale_links(root, changed)


if __name__ == "__main__":
    main()
