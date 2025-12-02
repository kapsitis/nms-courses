$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

# Capture the script name for usage text
$scriptName = Split-Path -Leaf $PSCommandPath

function Show-Usage {
    Write-Host "Usage: $scriptName input.md [output.pdf]"
    exit 1
}

# Require 1 or 2 args
if ($args.Count -lt 1 -or $args.Count -gt 2) {
    Show-Usage
}

$in = $args[0]

# Input must exist and be a file
if (-not (Test-Path -Path $in -PathType Leaf)) {
    Write-Error "Input not found: $in"
    exit 2
}

# Derive output if not provided
if ($args.Count -eq 2) {
    $out = $args[1]
} else {
    # Replace extension with .pdf
    $out = [System.IO.Path]::ChangeExtension($in, 'pdf')
}

# If output is a directory, write inside it with this odd "truncated" logic
if (Test-Path -Path $out -PathType Container) {
    # Original bash:
    # truncated="${out}"
    # out="${out}/${truncated}.pdf"
    $truncated = $out
    $out = Join-Path $out "$truncated.pdf"
}

# Compute absolute directory of the input file
$indir = Split-Path -Path (Resolve-Path -LiteralPath $in) -Parent

# Invoke pandoc
& pandoc `
    "$in" `
    -o "$out" `
    --lua-filter=solutions.lua `
    "--resource-path=$indir" `
    --from "markdown+tex_math_dollars+pipe_tables" `
    --pdf-engine=lualatex `
    --template eisvogel `
    -V "colorlinks=true"

Write-Host "Wrote $out"