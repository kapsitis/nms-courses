#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil
import time
from pathlib import Path

def get_timestamp(path):
    return path.stat().st_mtime

def needs_update(source_path, dest_path):
    if not dest_path.exists():
        return True
    return get_timestamp(source_path) > get_timestamp(dest_path)

def run_pandoc(input_file, output_file, resource_path, show_solutions, lua_filter_path):
    """
    Runs pandoc to convert input_file to output_file.
    """
    cmd = [
        "pandoc",
        str(input_file),
        "-o", str(output_file),
        f"--lua-filter={lua_filter_path}",
        f"--resource-path={resource_path}",
        "--from", "markdown+tex_math_dollars+pipe_tables",
        "--pdf-engine=lualatex",
        "--template", "eisvogel",
        "-V", "colorlinks=true",
        "-M", f"show-solutions={str(show_solutions).lower()}"
    ]
    
    print(f"Generating {output_file} (Solutions: {show_solutions})...")
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error generating {output_file}: {e}", file=sys.stderr)
        return False

def process_directory(parent_dir, output_dir_base):
    parent_path = Path(parent_dir)
    if not parent_path.exists():
        print(f"Error: Input directory '{parent_dir}' does not exist.")
        sys.exit(1)

    # Determine default output directory if not provided
    if output_dir_base:
        output_path = Path(output_dir_base)
    else:
        # Default: docs/<parent_dir_name>
        output_path = Path("docs") / parent_path.name

    output_path.mkdir(parents=True, exist_ok=True)

    # Locate solutions.lua
    # 1. Try inside parent_dir
    lua_filter = parent_path / "solutions.lua"
    # 2. Try online-tests/solutions.lua as fallback
    if not lua_filter.exists():
         lua_filter = Path("online-tests/solutions.lua")
    
    if not lua_filter.exists():
        print(f"Warning: 'solutions.lua' not found in {parent_path} or 'online-tests'. Processing might fail or ignore solutions.")

    success_count = 0
    skip_count = 0
    error_count = 0

    # Iterate over subdirectories
    for child in parent_path.iterdir():
        if child.is_dir():
            content_md = child / "content.md"
            if content_md.exists():
                subdir_name = child.name
                
                # Targets
                pdf_no_solutions = output_path / f"{subdir_name}.pdf"
                pdf_with_solutions = output_path / f"{subdir_name}-solutions.pdf"

                # Process No Solutions
                if needs_update(content_md, pdf_no_solutions):
                    if run_pandoc(content_md, pdf_no_solutions, child, False, lua_filter):
                        success_count += 1
                    else:
                        error_count += 1
                else:
                    print(f"Skipping {pdf_no_solutions} (up to date)")
                    skip_count += 1

                # Process With Solutions
                if needs_update(content_md, pdf_with_solutions):
                    if run_pandoc(content_md, pdf_with_solutions, child, True, lua_filter):
                        success_count += 1
                    else:
                        error_count += 1
                else:
                    print(f"Skipping {pdf_with_solutions} (up to date)")
                    skip_count += 1

    print(f"\nProcessing complete.")
    print(f"Generated: {success_count}")
    print(f"Skipped:   {skip_count}")
    print(f"Errors:    {error_count}")

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python process_pdf.py <input_dir> [output_dir]")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) == 3 else None

    process_directory(input_dir, output_dir)

if __name__ == "__main__":
    main()
