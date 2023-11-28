import glob 
import os
# script to run all cases
files_to_run = []

for filename in glob.glob('data/zad2/*'):
    files_to_run.append(filename)
for filename in glob.glob('data/zad1/*'):
    files_to_run.append(filename)
for filename in glob.glob('data/zad3/*'):
    files_to_run.append(filename)
for filename in glob.glob('data/zad4/*'):
    files_to_run.append(filename)
for filename in glob.glob('data/zad5/*'):
    files_to_run.append(filename)
for filename in glob.glob('data/zad6/*'):
    files_to_run.append(filename)

for file in files_to_run:
    os.system(f'java tiny_gp.java {file}')
