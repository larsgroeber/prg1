from glob import glob

import re

from author_class import Author
from util import value_question


class HeaderAdder:
    def __init__(self):
        self.__authors = self.__get_authors_from_user()
        self.__email = self.__get_email_from_user()
        self.__credits = self.__get_credits_from_user()
        
    def add_headers(self, path):
        python_files = glob(path + '/*.py')
        if len(python_files) == 0:
            print('No python files found!')
            exit(1)
        self.__add_headers_to_files(python_files)

    def __add_headers_to_files(self, python_files):
        for file in python_files:
            with open(file, 'r+') as f:
                content_lines = f.read().splitlines()
                if len(content_lines) == 0:
                    print(f'File "{file}" is empty!')
                    continue
                if not self.__does_file_has_docstring(content_lines):
                    print(f'File "{file}" has no docstring!')
                index_after_imports = self.__index_for_variables(content_lines)
                content_before_vars = content_lines[:index_after_imports]
                content_after_vars = content_lines[index_after_imports:]
                vars_content = ['', ''] + self.__construct_variables().split('\n')
                new_content = content_before_vars + vars_content + content_after_vars
                f.seek(0, 0)
                f.write('\n'.join(new_content))

    def get_authors(self):
        return self.__authors

    def __get_authors_from_user(self):
        num_authors = int(value_question('How many authors were working on this project?', type='int', default=1))
        if num_authors < 1:
            exit(1)
        authors = []
        for i in range(1, num_authors + 1):
            print(f'Please enter the information for the {i}. author:')
            matrikel = value_question('Matrikelnumber: ')
            surname = value_question('Surname: ')
            name = value_question('Lastname: ')
            authors.append(Author(matrikel, name, surname))
        return authors
    
    def __get_email_from_user(self):
        return value_question('What is your email? ')

    def __get_credits_from_user(self):
        return value_question('If you want to add credits, enter them here:', default="")

    def __read_file(self, path: str):
        with open(path, 'r+') as f:
            return f.read()

    def __construct_variables(self):
        vars = '__author__ = "{}"\n'    .format(self.__build_author())
        vars += '__copyright__ = "{}"\n'.format(self.__get_copyright())
        vars += '__credits__ = "{}"\n'  .format(self.__credits) if self.__credits else ''
        vars += '__email__ = "{}"\n'   .format(self.__email)
        return vars

    def __build_author(self):
        author_strings = list(map(lambda a: f"{a.matrikel}: {a.surname} {a.name}", self.__authors))
        return ', '.join(author_strings)

    def __get_copyright(self):
        return "Copyright 2017/2018 – EPR-Goethe-Uni"

    def __index_for_variables(self, content_lines: [str]):
        index = 0
        for i, line in enumerate(content_lines):
            line = line.strip()
            if re.match('^(import|from)\s', line) is not None:
                index = i
        # if there is no import/from statement
        if index == 0:
            if self.__does_file_has_docstring(content_lines):
                if re.match('^(\"\"\"|\'\'\').*(\"\"\"|\'\'\')', content_lines[0].strip()) is not None:
                    return 1
                docstring_indexes = [i for i, l in enumerate(content_lines)
                                   if re.match('^(\"\"\"|\'\'\')', l.strip()) is not None]
                return docstring_indexes[1] + 1
            return 0
        return index + 1

    def __does_file_has_docstring(self, content_lines: [str]):
        for line in content_lines:
            line = line.strip()
            if re.match('^(\"\"\"|\'\'\')', line) is not None:
                return True
            if line != "":
                return False
