import os
import re


def findInlineStylesFromCSS(file):
    regex = r'(?:export )*const [a-zA-z0-9]+ = {.+?(?=};)};'
    return re.findall(regex, file, re.MULTILINE|re.DOTALL)


for currentpath, folders, files in os.walk('./input'):
    for file in files:
        path = (os.path.join(currentpath, file))
        open_file = open(path, 'r')
        read_file = open_file.read()
        matches = findInlineStylesFromCSS(read_file)
        for match in matches:
            read_file = read_file.replace(match,'')
        write_file = open(path, 'w')
        write_file.write(read_file)

