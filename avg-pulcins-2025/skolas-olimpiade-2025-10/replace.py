import re

with open ('_build/latex/skolas-olimpiade-2025-10.tex', 'r', encoding='utf-8') as f:
    content = f.read()
    content = re.sub(r'\\sphinxAtStartPar[\s\n]*\\sphinxstylestrong\{Atbilde:\}',
        r'\\sphinxAtStartPar\n{\\color{blue}\n\\sphinxstylestrong{Atbilde:}', content, flags = re.M)

    content = re.sub(r'\\sphinxAtStartPar[\s\n]*\\sphinxstylestrong\{Ieteikums:\}',
        r'\\sphinxAtStartPar\n{\\color{blue}\n\\sphinxstylestrong{Ieteikums:}', content, flags = re.M)

    content = re.sub(r'\\sphinxAtStartPar[\s\n]*\\\(\\square\\\)[\s\n]*',
        r'}% end blue\n', content, flags = re.M)


with open ('_build/latex/skolas-olimpiade-2025-10.tex', 'w', encoding='utf-8') as fout:
    fout.write(content)
    fout.close
