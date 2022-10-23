import os
from pathlib import Path
import shutil

src = ['other',
        '../ntjun-textbook/ntjun01-divisibility',
        '../ntjun-textbook/ntjun02-modular-arithmetic',
        '../ntjun-textbook/ntjun03-crt',
        '../ntjun-textbook/ntjun04-multiplicative',
        '../ntjun-textbook/ntjun05-valuations',
        '../ntjun-textbook/ntjun06-rational',
        '../ntjun-textbook-single',
        '../regional-workshops',
        '../problems/selection_problems_2020_2021',
        '../onlinetests']


dest = '/var/www/html/training/numtheory'

for src_dir in src:
    files = os.listdir(src_dir)

    for fname in files:
        if fname.endswith('.pdf') or fname.endswith('.pptx'):
            shutil.copy2(os.path.join(src_dir,fname),dest)

# Need to publish all PDF files that are located in the subdirectories of these superdirectories.
superDirs = ['../imo-team-trainings',
        '../homeworks', 
        '../problems/selection_problems_2022_2023']

for super_dir in superDirs:
    for subdir, dirs, files in os.walk(super_dir):
        for file in files:
            if file.endswith('.pdf'):
                shutil.copy2(os.path.join(subdir,file),dest)
