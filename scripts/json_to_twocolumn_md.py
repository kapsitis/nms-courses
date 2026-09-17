#!/usr/bin/env python3
"""Turn a JSON problem list into a two-column Markdown worksheet.

The input looks like questiontype_problems.json:

    {
      "title": "9.1. Atrisinājumu struktūras: Uzdevumi",   (optional)
      "intro": "Uzdevumi dažādiem jautājumu tipiem...",    (optional)
      "problems": [
        {"problemID": "1", "problemText_lv": "Kāds cipars ...", "imageWidth": 130}
      ]
    }

``imageWidth`` (optional, pixels) sizes an ``![](...)`` inside that problem.

The problems are laid out like the printed worksheets: a two-column table whose
left column holds the first half of the list (1-12) and whose right column holds
the second (13-24), each cell starting with the problem number in bold. Newlines
inside a problem become ``<br>``, so a problem -- its image included -- stays in
a single table cell.

The Jekyll front-matter is derived from the OUTPUT path: the permalink mirrors
the file's location in the site and the docx_*/geometry keys are the defaults
from fix_permalinks.py, so the page can be converted by convert_directory.py
right away.

Usage:
    python scripts/json_to_twocolumn_md.py <json-input> <md-output>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from convert_directory import site_root
from fix_permalinks import docx_defaults, expected_permalink, yaml_value

_IMAGE = re.compile(r"!\[[^\]]*\]\([^)]*\)")


def problem_number(problem: dict) -> str:
    return str(problem.get("problemID") or problem.get("id") or "?")


def problem_cell(problem: dict) -> str:
    """One table cell: '**(3)** text', with newlines folded into <br>."""
    text = (problem.get("problemText_lv") or problem.get("problemText")
            or problem.get("text") or "").strip()
    width = problem.get("imageWidth")
    if width:
        # kramdown IAL; md_to_docx translates it for pandoc (.docx and .pdf).
        text = _IMAGE.sub(lambda m: f'{m.group(0)}{{: width="{width}"}}', text)
    text = re.sub(r"\n+", "<br>", text)
    # A lone '*' (as in "987*") would otherwise start Markdown emphasis, and a
    # '|' would end the cell. Escape both before adding our own bold marks.
    text = text.replace("|", r"\|").replace("*", r"\*")
    return f"**({problem_number(problem)})** {text}"


def two_column_table(problems: list[dict], heading: str = "Uzdevumi") -> list[str]:
    """Rows of a 2-column table: first half left, second half right."""
    half = (len(problems) + 1) // 2
    left, right = problems[:half], problems[half:]

    def label(group: list[dict]) -> str:
        return (f"{heading} {problem_number(group[0])}.–{problem_number(group[-1])}."
                if group else "")

    rows = [f"| {label(left)} | {label(right)} |", "|:---|:---|"]
    for index in range(half):
        right_cell = problem_cell(right[index]) if index < len(right) else ""
        rows.append(f"| {problem_cell(left[index])} | {right_cell} |")
    return rows


def front_matter(md_path: Path, title: str) -> list[str]:
    """Jekyll + docx front-matter for a page at ``md_path``."""
    lines = ["---", "layout: default", f"title: {yaml_value(title)}"]
    root = site_root(md_path.parent)
    if root:
        lines.append(f"permalink: {expected_permalink(md_path, root)}")
    lines.append("")
    lines += [f"{key}: {yaml_value(value)}"
              for key, value in docx_defaults(md_path, title).items()]
    lines.append("---")
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a JSON problem list into a two-column Markdown page."
    )
    parser.add_argument("json_input", help="JSON file with a 'problems' list")
    parser.add_argument("md_output", help="Markdown file to write (overwritten)")
    args = parser.parse_args()

    json_path, md_path = Path(args.json_input), Path(args.md_output)
    if not json_path.exists():
        sys.exit(f"Input file not found: {json_path}")
    data = json.loads(json_path.read_text(encoding="utf-8-sig"))
    problems = data.get("problems") if isinstance(data, dict) else data
    if not problems:
        sys.exit(f"No problems found in {json_path}")

    title = data.get("title", md_path.stem.capitalize()) if isinstance(data, dict) else md_path.stem
    intro = data.get("intro", "") if isinstance(data, dict) else ""
    lines = front_matter(md_path, title) + ["", f"# {title}", ""]
    if intro:
        lines += [intro, ""]
    lines += two_column_table(problems)

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"Wrote {md_path}: {len(problems)} problems in 2 columns")


if __name__ == "__main__":
    main()
