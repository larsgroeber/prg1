#!/usr/bin/env python
import glob
import sys
import os
import shutil

from author import MATRIKEL, FIRSTNAME, LASTNAME


def add_author_variable(filename):
    with open(filename, 'r+') as f:
        content = f.read()
        author_variable = "__author__ = \"{}: {} {}\"".format(MATRIKEL, FIRSTNAME, LASTNAME)
        if len(content) > 0 and author_variable not in content[:10]:
            f.seek(0, 0)
            f.write(author_variable + "\n\n\n" + content)


if len(sys.argv) != 3:
    print("Usage: {} SHEET_DIRECTORY SHEET_NUMBER".format(sys.argv[0]))
    exit(0)

if FIRSTNAME == "" or LASTNAME == "" or MATRIKEL == "":
    print("Please copy 'author.default.py' to 'author.py' and add your credentials!")
    exit(-1)


SHEETNUMBER = sys.argv[2]
directory_path: str = sys.argv[1]

directory_name = directory_path.split("/")[-1]
base_directory = "/".join(directory_path.split("/")[:-1])
final_directory_path = base_directory + "/" + directory_name + ".final"

print("Creating directory {}".format(final_directory_path))
os.makedirs(final_directory_path, exist_ok=True)

python_files = glob.glob(directory_path + "/*.py")
pdf_files = glob.glob(directory_path + "/*.pdf")

print("Copying files")
for file in python_files + pdf_files:
    new_file = final_directory_path + "/{}_{}_".format(FIRSTNAME, LASTNAME) + file.split("/")[-1]
    shutil.copyfile(file, new_file)

print("Adding __author__ variable")
for file in python_files:
    new_file = final_directory_path + "/{}_{}_".format(FIRSTNAME, LASTNAME) + file.split("/")[-1]
    add_author_variable(new_file)

print("Zipping")
shutil.make_archive(base_directory + "/EPR_Blatt_{}_{}_{}".format(SHEETNUMBER, FIRSTNAME, LASTNAME),
                    "zip",
                    final_directory_path)

print("Removing {}".format(final_directory_path))
shutil.rmtree(final_directory_path)
