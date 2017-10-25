__author__ = ""
#!/usr/bin/env python
import glob
import sys

import os


def add_author_variable(filename):
    with open(filename, 'r+') as f:
        content = f.read()
        if len(content) > 0 and "__author__" not in content[:10]:
            f.seek(0, 0)
            f.write("__author__\n" + content)


directory = sys.argv[1]

python_files = glob.glob(directory + "/*.py")
for file in python_files:
    add_author_variable(file)