import re
with open ('_build/latex/nms-imo-izlase-2022b.tex', 'r', encoding='utf-8') as f:
    content = f.read()
    content_new = re.sub(r'\\sphinxAtStartPar[\s\n]*\\sphinxstylestrong\{Answer:\}',
        r'\\sphinxAtStartPar\n{\\color{blue}\n\\sphinxstylestrong{Answer:}', content, flags = re.M)
    content_new = re.sub(r'\\sphinxAtStartPar[\s\n]*\\sphinxstylestrong\{Atbilde:\}',
        r'\\sphinxAtStartPar\n{\\color{blue}\n\\sphinxstylestrong{Atbilde:}', content, flags = re.M)
    #content_new = re.sub(r'\\sphinxAtStartPar[\s\n]*\\\(\\square\\\)[\s\n]*',
    #    r'\\sphinxAtStartPar\n\\(\\square\\)\n}% end blue\n', content_new, flags = re.M)
    content_new = re.sub(r'\\sphinxAtStartPar[\s\n]*\\\(\\square\\\)[\s\n]*',
        r'}% end blue\n', content_new, flags = re.M)


with open ('_build/latex/nms-imo-izlase-2022b.tex', 'w', encoding='utf-8') as fout:
    fout.write(content_new)
    fout.close
