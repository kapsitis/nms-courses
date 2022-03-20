import os
from pathlib import Path
import shutil 

src = ['../homeworks/homework01', 
        '../homeworks/homework02',
        '../homeworks/homework03',
        '../homeworks/homework04',
        '../homeworks/homework05',
        '../homeworks/homework06', 
        '../exams',
        '../midterm',
        '../final',
        '../proofs',
        '../quizzes']


dest = '/var/www/html/training/discrete-2022-spring' 

for src_dir in src:
    files = os.listdir(src_dir)

    for fname in files:
        if fname.endswith('.pdf'):
            shutil.copy2(os.path.join(src_dir,fname),dest)

