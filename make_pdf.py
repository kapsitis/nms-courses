#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path

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

def main():
    if len(sys.argv) != 3:
        print("Usage: python make_pdf.py <input_dir> <questions|solutions>")
        sys.exit(1)

    input_dir_str = sys.argv[1]
    mode = sys.argv[2].lower()

    if mode not in ["questions", "solutions"]:
        print("Error: Second argument must be 'questions' or 'solutions'")
        sys.exit(1)

    input_path = Path(input_dir_str)
    if not input_path.exists() or not input_path.is_dir():
        print(f"Error: Input directory '{input_dir_str}' does not exist or is not a directory.")
        sys.exit(1)

    content_md = input_path / "content.md"
    if not content_md.exists():
        print(f"Error: {content_md} not found.")
        sys.exit(1)

    dirname = input_path.name

    # Determine output filename and show_solutions flag
    if mode == "questions":
        output_file = input_path / f"{dirname}.pdf"
        show_solutions = False
    else:
        output_file = input_path / f"{dirname}-solutions.pdf"
        show_solutions = True

    # Locate solutions.lua
    # 1. Try inside input_dir
    lua_filter = input_path / "solutions.lua"
    # 2. Try online-tests/solutions.lua as fallback relative to script location
    # Assuming script is in root of nms-courses, online-tests should be in same dir
    script_dir = Path(__file__).resolve().parent
    if not lua_filter.exists():
         lua_filter = script_dir / "online-tests" / "solutions.lua"
         if not lua_filter.exists():
             # Last resort, check if we are running from somewhere else and online-tests is in current dir
             lua_filter = Path("online-tests/solutions.lua")

    if not lua_filter.exists():
        print(f"Warning: 'solutions.lua' not found in {input_path} or '{script_dir}/online-tests'. Processing might fail or ignore solutions.")

    run_pandoc(content_md, output_file, input_path, show_solutions, lua_filter)

if __name__ == "__main__":
    main()
