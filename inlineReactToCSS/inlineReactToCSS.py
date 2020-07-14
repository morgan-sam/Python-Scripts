import os
import re

for currentpath, folders, files in os.walk('./input'):
    for file in files:
        path = (os.path.join(currentpath, file))
        open_file = open(path, 'r')
        read_file = open_file.read()

        # format obj name / classname
        regex = re.compile(
            '(?:export )*const ([a-zA-z0-9]+) = ({.+?(?=};)};)', flags=re.MULTILINE | re.DOTALL)
        read_file = regex.sub('\\1: \\2', read_file)

        write_file = open(path, 'w')
        write_file.write(read_file)
