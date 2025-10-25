import sys
import os

# Append the path to the script directory
sys.path.append(os.path.abspath('../../../math/src/site/problembase/scripts'))

from proc_parse_translate import extract_sections_from_md

def remove_small_tag(text):
    meta_start = text.find('<small>')
    if meta_start > 0:
        text = text[0:meta_start]
    return text

if __name__ == '__main__':
    if len(sys.argv) < 2: 
        print("Usage: python questions_only.py <directoryname-with-content-md>")
        sys.exit(1)
    file_name = f"{sys.argv[1]}/content.md"
    problemList = extract_sections_from_md(file_name)
    for (title, problem) in problemList:
        problem = remove_small_tag(problem)
        print(problem)
        print()

# python questions_only.py lv-avgtest-2024c > lv-avgtest-2024c/content-questions-only.md
# pandoc lv-avgtest-2024c/content-questions-only.md -o lv-avgtest-2024c/lv-avgtest-2024c-pigeonhole.pdf --pdf-engine=xelatex
# pandoc content.md -o lv-avgtest-2024c-pigeonhole-solved.pdf --pdf-engine=xelatex
