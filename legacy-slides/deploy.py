import os
from pathlib import Path
import shutil 

src = ['other', 
        '../ntjun-textbook/ntjun01-divisibility/_build/latex',
        '../homeworks/homework03/_build/latex',
        '../homeworks/homework04/_build/latex',
        '../homeworks/homework05/_build/latex']




dest = '/var/www/html/training/numtheory' 

for src_dir in src:
    files = os.listdir(src_dir)

    for fname in files:
        if fname.endswith('.pdf') or fname.endswith('.pptx'):
            shutil.copy2(os.path.join(src_dir,fname),dest)

