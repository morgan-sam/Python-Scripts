import os
import re

for currentpath, folders, files in os.walk('./input'):
    for file in files:
        path = (os.path.join(currentpath, file))
        open_file = open(path, 'r')
        read_file = open_file.read()
        print(read_file)
        regex = r'(?:export )*const [a-zA-z0-9]+ = {.+?(?=};)};'
        matches = re.findall(regex, read_file, re.MULTILINE|re.DOTALL)
        for match in matches:
            read_file = read_file.replace(match,'')            
        print(read_file)
        print(matches)
        write_file = open(path, 'w')
        write_file.write(read_file)
