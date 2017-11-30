#!/usr/bin/env python
import glob
import sys
import os
import shutil

import util
from header_adder import HeaderAdder

if len(sys.argv) != 3:
    print("Usage: {} SHEET_DIRECTORY SHEET_NUMBER".format(sys.argv[0]))
    exit(0)

print()
print('For which module is this directory a solution?')
module_menu = {'1': 'PRG', '2': 'EPR'}
module_name = module_menu[util.menu(module_menu)]

header_adder = HeaderAdder()

SHEETNUMBER = sys.argv[2]
directory_path: str = sys.argv[1]

if directory_path[0] not in ['.', '/']:
    directory_path = './' + directory_path

directory_name = directory_path.split("/")[-1]
base_directory = "/".join(directory_path.split("/")[:-1])
final_directory_path = base_directory + "/" + directory_name + ".final"

print("\nCreating directory {}".format(final_directory_path))
os.makedirs(final_directory_path, exist_ok=True)

globs = ['*.py', '*.pdf', '*.md', '*.txt']
files = []
for g in globs:
    files.extend(glob.glob(directory_path + "/" + g))

author_names = ""
for author in header_adder.get_authors():
    author_names += "{}_{}_".format(author.surname, author.name)
author_names = author_names[:-1]  # remove last _

print(f"\nCopying files to {final_directory_path}")
for file in files:
    new_file = final_directory_path + "/" + author_names + '_' + file.split("/")[-1]
    shutil.copyfile(file, new_file)

print("\nAdding variables")
header_adder.add_headers(final_directory_path)

zip_archive = base_directory + "/{}_Blatt_{}_{}".format(module_name, SHEETNUMBER, author_names)
print(f"\nZipping to '{zip_archive}'")
shutil.make_archive(zip_archive,
                    "zip",
                    final_directory_path)

print("\nRemoving '{}'".format(final_directory_path))
shutil.rmtree(final_directory_path)
print("Done")
print("\nYou find your zip file here:", zip_archive + '.zip')
