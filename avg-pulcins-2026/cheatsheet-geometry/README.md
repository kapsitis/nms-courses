# Building Cheatsheet Geometry

This document outlines how to compile the `cheatsheet-geometry.tex` file into a PDF using [MiKTeX](https://miktex.org/).

## Prerequisites

- **MiKTeX** must be installed on your system.

## Build Instructions

1. Open your command line (Command Prompt or PowerShell).
2. Navigate to this directory (`avg-pulcins-2026/cheatsheet-geometry`).
3. Run the following command to compile the LaTeX document:

```powershell
xelatex cheatsheet-geometry.tex
```

*(Note: The `cheatsheet-geometry.tex` file includes packages like `fontspec` and `polyglossia`, which makes `xelatex` the appropriate LaTeX engine to use.)*

4. Run the command a second time to ensure that all internal structures, tables, and formatting are correctly aligned and built:

```powershell
xelatex cheatsheet-geometry.tex
```

## Output

After successful compilation, the `cheatsheet-geometry.pdf` file will be generated in the same directory along with some auxiliary files (such as `.log` and `.aux`).
