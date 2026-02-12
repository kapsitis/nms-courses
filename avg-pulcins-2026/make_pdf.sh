#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $(basename "$0") <input> <output> <questions|solutions>"
  exit 1
}

# Require exactly 3 args
(( $# != 3 )) && usage

in="$1"
[[ -f "$in" ]] || { echo "Input not found: $in" >&2; exit 2; }

out="$2"
mode="$3"

if [[ "$mode" != "questions" && "$mode" != "solutions" ]]; then
  echo "Error: Third argument must be 'questions' or 'solutions'" >&2
  usage
fi

# If output is a directory, write inside it with input’s basename
if [[ -d "$out" ]]; then
  # truncated="${out:11}"
  truncated="${#out}"
  # Wait, the logic regarding truncation in original file seemed specific or commented out.
  # The original had:
  # truncated="${out}"
  # out="${out}/${truncated}.pdf"
  # This looks like it tries to use the directory name as the filename? Or maybe there was a variable missing.
  # Let's stick to a safe default: use input filename base.
  base=$(basename "$in")
  out="${out}/${base%.*}.pdf"
fi

indir="$(cd "$(dirname "$in")" && pwd)"

common_args=(
  "$in"
  -o "$out"
  --resource-path="$indir"
  --from "markdown+tex_math_dollars+grid_tables"
  --pdf-engine=lualatex
  --template eisvogel
  -V colorlinks=true
)

echo "Generating PDF for $mode..."

if [[ "$mode" == "questions" ]]; then
  pandoc "${common_args[@]}" --lua-filter <(echo "function Div(el) if el.classes:includes('solution') then return {} end end")
else
  pandoc "${common_args[@]}"
fi

echo "Wrote $out"
