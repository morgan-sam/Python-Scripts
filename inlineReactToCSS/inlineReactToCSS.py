import os
import re
import os

def findInlineStylesFromCSS(file):
    regex = r'(?:export )*const [a-zA-z0-9]+ = {.+?(?=};)};'
    return re.findall(regex, file, re.MULTILINE|re.DOTALL)

def removeSpeechMarks(inlines):
    return map(lambda x:re.sub(r'[\'\`]','',x),inlines)

def replaceCommasWithColons(inlines):
    return map(lambda x:re.sub(r',\n',';\n',x),inlines)

os.system("./resetInput.sh")
os.system("prettier --write ./input/*")

for currentpath, folders, files in os.walk('./input'):
    for file in files:
        path = (os.path.join(currentpath, file))
        open_file = open(path, 'r')
        read_file = open_file.read()
        inlines = findInlineStylesFromCSS(read_file)
        for match in inlines:
            read_file = read_file.replace(match,'')
        write_file = open(path, 'w')
        write_file.write(read_file)

inlines = removeSpeechMarks(inlines)
print(inlines)
inlines = replaceCommasWithColons(inlines)
for inline in inlines:
    print(inline)
