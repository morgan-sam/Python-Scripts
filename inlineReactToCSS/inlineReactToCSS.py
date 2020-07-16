import os
import re
import sys


def getDirectory():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return '.'


def fileConstDic(file):
    regex = r'(?:export )*const ([A-Z_]+) = ([a-zA-Z0-9_\-\'\"\`]+);'
    constants = re.findall(regex, file, re.MULTILINE | re.DOTALL)
    return {constants[i][0]: constants[i][1] for i in range(0, len(constants))} 

def getNonExportConstants(file):
    regex = r'^(?!export )const ([A-Z_]+) = [a-zA-Z0-9_\-\'\"\`]+;$'
    return re.findall(regex, file, re.MULTILINE | re.DOTALL)

def usedConstInlines(inlines, constants):
    varNames = list(constants.keys())
    allInlines = ''.join(inlines)
    used = filter(lambda x: allInlines.find(x) != -1, varNames)
    return {key: constants[key] for key in used}


def findInlineStylesFromCss(file):
    regex = r'(?:export )*const [a-zA-z0-9]+ = {.+?(?=};)};'
    return re.findall(regex, file, re.MULTILINE | re.DOTALL)

def addCssVarsToInline(inline, constDic):
    keys = list(constDic.keys())
    for i in range(len(keys)):
        regex = re.compile('(?:\\$\\{)*'+keys[i]+'(?:\\})*')
        inline = re.sub(regex, 'var(--{})'.format(constToCssVarFormat(keys[i])), inline)
    return inline

def removeSpeechMarks(inlines):
    return map(lambda x: re.sub(r'[\'\`]', '', x), inlines)


def replaceCommasWithColons(inlines):
    return map(lambda x: re.sub(r',\n', ';\n', x), inlines)


def removeCamelCase(inlines):
    return map(lambda x: re.sub(r'([A-Z])', lambda x: '-'+x.group(0).lower(), x), inlines)


def convertToClassName(inlines):
    return map(lambda x: re.sub(r'(?:export )*const ([a-zA-z0-9\-]+) = ', '.\\1 ', x), inlines)

def constToCssVarFormat(const):
    return re.sub(r'_','-',const.lower())


def inlineStylesToCss(styles, constDic):
    styles = map(lambda x: addCssVarsToInline(x, constDic), styles)
    styles = removeSpeechMarks(styles)
    styles = replaceCommasWithColons(styles)
    styles = removeCamelCase(styles)
    return convertToClassName(styles)

def convertConstDicToCssVars(constDic):
    return map(lambda x: '--{}: {};'.format(constToCssVarFormat(x[0]),x[1]), constDic.items())


def convertInlinesToCssFile(file, inlines, constDic):
    if (len(inlines)):
        newFileName = re.sub(r'.js', '.css', file)
        styles = inlineStylesToCss(inlines, constDic)
        cssVars = convertConstDicToCssVars(constDic)
        with open(os.path.join(currentpath, newFileName), 'a+') as f:
            if (len(cssVars)):
                f.write(":root {\n")
                for var in cssVars:
                    f.write("    %s\n" % var)
                f.write("}\n\n")
            for style in styles:
                f.write("%s\n\n" % style)

def removeUnusedConsts(read_file):
    keys = getNonExportConstants(read_file)
    for i in range(len(keys)):
        if (len(re.findall(keys[i], read_file)) < 2):
            read_file = re.sub(r'const {} = ([a-zA-Z0-9_\-\'\"\`]+);'.format(keys[i]), '', read_file)
    return read_file


def writeToJsFile(read_file, inlines, path):
    for match in inlines:
        read_file = read_file.replace(match, '').strip()
    read_file = removeUnusedConsts(read_file)
    if (len(read_file) > 0):
        write_file = open(path, 'w')
        write_file.write(read_file)
    else:
        os.remove(path)


dir = getDirectory()
os.system('prettier --write {}/*.js'.format(dir))


for currentpath, folders, files in os.walk(dir):
    for file in files:
        if file.endswith(".js"):
            path = (os.path.join(currentpath, file))
            read_file = open(path, 'r').read()
            constants = fileConstDic(read_file)
            inlines = findInlineStylesFromCss(read_file)
            constInlines = usedConstInlines(inlines, constants)
            writeToJsFile(read_file, inlines, path);

            convertInlinesToCssFile(file, inlines, constInlines)
