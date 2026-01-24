#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $(basename "$0") input.md [output.pdf]"
  exit 1
}

# Require 1 or 2 args
(( $# < 1 || $# > 2 )) && usage

in="$1"
[[ -f "$in" ]] || { echo "Input not found: $in" >&2; exit 2; }

# Derive output if not provided
if (( $# == 2 )); then
  out="$2"
else
  out="${in%.*}.pdf"
fi

# If output is a directory, write inside it with input’s basename
if [[ -d "$out" ]]; then
#  out="$out/$(basename "${in%.*}").pdf"
  # truncated="${out:11}"
  truncated="${out}"
  out="${out}/${truncated}.pdf"
fi

# # Ensure .pdf extension
# case "$out" in
#   *.pdf) ;;
#   *) out="${out}.pdf" ;;
# esac

indir="$(cd "$(dirname "$in")" && pwd)"

## --from markdown+tex_math_dollars+pipe_tables \
# To skip solutions in livani-2026-01-24.md, add the following to the pandoc command:
# --lua-filter <(echo "function Div(el) if el.classes:includes('solution') then return {} end end") \

pandoc "$in" -o "$out" \
  --resource-path="$indir" \
  --from markdown+tex_math_dollars+grid_tables \
  --pdf-engine=lualatex \
  --template eisvogel \
  -V colorlinks=true
  # --lua-filter <(echo "function Div(el) if el.classes:includes('solution') then return {} end end") \
  

echo "Wrote $out"

