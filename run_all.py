import glob 
import os
# script to run all cases
files_to_run = []
# all files in data/zad1, data/zad4, data/zad6
for filename in glob.glob('data/zad1/*'):
    files_to_run.append(filename)
for filename in glob.glob('data/zad4/*'):
    files_to_run.append(filename)
for filename in glob.glob('data/zad6/*'):
    files_to_run.append(filename)

for file in files_to_run:
    os.system(f'java tiny_gp.java {file}')
