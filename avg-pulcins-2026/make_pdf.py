#!/usr/bin/env python3
import sys
import os
import subprocess

def usage():
    prog = os.path.basename(sys.argv[0])
    print(f"Usage: {prog} input.md [output.pdf|outputdir]", file=sys.stderr)
    sys.exit(1)


def get_params():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        usage()

    infile = sys.argv[1]

    if not os.path.isfile(infile):
        print(f"Input not found: {infile}", file=sys.stderr)
        sys.exit(2)

    if len(sys.argv) == 3:
        out = sys.argv[2]
    else:
        out = os.path.splitext(infile)[0] + ".pdf"

    if os.path.isdir(out):
        # The user gave a directory to store the PDF
        out = os.path.join(out, os.path.splitext(os.path.basename(infile))[0] + ".pdf")

    return infile, out    



def convert(infile, out):
    indir = os.path.abspath(os.path.dirname(infile))
    pandoc_cmd = [
        "pandoc",
        infile,
        "-o", out,
        f"--resource-path={indir}",
        "--from=markdown+tex_math_dollars+pipe_tables",
        "--pdf-engine=lualatex",
        "--template=eisvogel",
        "-V", "colorlinks=true"
    ]

    # Run Pandoc (fail if error)
    try:
        subprocess.run(pandoc_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Pandoc: {e}", file=sys.stderr)
        sys.exit(3)

    print(f"Wrote {out}")


if __name__ == '__main__': 
    infile, out = get_params()
    convert(infile, out)

