# How to build PDFs with Eisvogel template

```
PDD="$(pandoc --version | sed -n 's/^User data directory: //p')"

mkdir -p "$PDD/templates"

# unzip Eisvogel.zip - see https://github.com/Wandmalfarbe/pandoc-latex-template
# and copy to "$PDD/templates"
# eisvogel.beamer; eisvogel.latex

sudo tlmgr install \
amsmath fontspec unicode-math microtype geometry fancyhdr hyperref xcolor \
bookmark babel csquotes booktabs longtable array caption tcolorbox upquote

pandoc sample.md -o sample.pdf --from markdown+tex_math_dollars+pipe_tables --pdf-engine=lualatex --template eisvogel -V colorlinks=true

pandoc input.md -o output.pdf --from markdown+tex_math_dollars+pipe_tables+link_attributes+implicit_figures --pdf-engine=lualatex --template eisvogel -V colorlinks=true

sudo tlmgr install footnotebackref
```