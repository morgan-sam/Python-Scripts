import os
import re
import os
import sys

def getDirectory():
    if len(sys.argv) > 1: return sys.argv[1]
    else: return '.'

def findInlineStylesFromCss(file):
    regex = r'(?:export )*const [a-zA-z0-9]+ = {.+?(?=};)};'
    return re.findall(regex, file, re.MULTILINE | re.DOTALL)

def removeSpeechMarks(inlines):
    return map(lambda x: re.sub(r'[\'\`]', '', x), inlines)

def replaceCommasWithColons(inlines):
    return map(lambda x: re.sub(r',\n', ';\n', x), inlines)

def removeCamelCase(inlines):
    return map(lambda x: re.sub(r'([A-Z])', lambda x: '-'+x.group(0).lower(), x), inlines)

def convertToClassName(inlines):
    return map(lambda x: re.sub(r'(?:export )*const ([a-zA-z0-9\-]+) = ', '.\\1 ', x), inlines)

def inlineStylesToCss(styles):
    styles = removeSpeechMarks(styles)
    styles = replaceCommasWithColons(styles)
    styles = removeCamelCase(styles)
    return convertToClassName(styles)

def convertInlinesToCssFile(file, inlines):
    newFileName = re.sub(r'.js', '.css', file)
    styles = inlineStylesToCss(inlines)
    with open(os.path.join(currentpath, newFileName), 'w') as f:
        for style in styles:
            f.write("%s\n" % style)

os.system("./resetInput.sh")
os.system("prettier --write ./input/*.js")

for currentpath, folders, files in os.walk('./input'):
    for file in files:
        if file.endswith(".js"):
            path = (os.path.join(currentpath, file))
            open_file = open(path, 'r')
            read_file = open_file.read()
            inlines = findInlineStylesFromCss(read_file)
            for match in inlines:
                read_file = read_file.replace(match, '')
            write_file = open(path, 'w')
            write_file.write(read_file)
            convertInlinesToCssFile(file, inlines)
