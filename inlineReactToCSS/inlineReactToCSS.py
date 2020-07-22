import os
import re
import sys
from itertools import chain


def getDirectory():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return '.'


def fileConstDic(file):
    regex = r'(?:export )*const ([a-zA-Z_]+) = ([a-zA-Z0-9_\-\'\"\`\#]+);'
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
    regex = r'(?:export )*const [a-zA-z0-9]+ = {(?:(?![^\'\`\"][a-zA-Z0-9]+?\(.*\)[^\'\`\"]).)*?};'
    return re.findall(regex, file, re.MULTILINE | re.DOTALL)


def addInlineToConvertedList(inline):
    regex = r'(?:export )*const ([a-zA-Z]+) = {'
    title = re.findall(regex, inline, re.MULTILINE | re.DOTALL)[0]
    if (len(title)):
        importList[file[:-3]].append(title)


def formatIfInlineSingleLine(inline):
    if(len(re.findall(r'\n', inline, re.MULTILINE)) == 0):
        regex = r'(?![a-zA-Z0-9, ]+\(),(?![a-zA-Z0-9, ]+\))'
        inline = re.sub(regex, ';', inline)
    return inline


def addCssVarsToInline(inline, constDic):
    keys = list(constDic.keys())
    for i in range(len(keys)):
        inline = re.sub(
            keys[i], 'var(--{})'.format(constToCssVarFormat(keys[i])), inline)
    return inline


def removeSpeechMarks(inline):
    return re.sub(r'[\'\`]', '', inline)


def replaceCommasWithColons(inline):
    return re.sub(r',\n', ';\n', inline)


def makeClassContentDic(styles):
    regex = r'(?:export )*const ([a-zA-Z]+) = \{((?:.|\n)*)(?:};)'
    matches = map(lambda x: (re.findall(regex, x, re.MULTILINE |
                                        re.DOTALL)[:1] or [None])[0], styles)
    matches = [i for i in matches if i]
    return {x[0]: {"content": x[1], "classes": [x[0]]} for x in matches}


def detectClassesInContent(dic):
    for entry in dic.items():
        for style in dic.keys():
            if (len(re.findall(style, entry[1]['content'])) > 0):
                dic[style]['classes'].append(entry[0])
                entry[1]['content'] = re.sub(
                    '...{};\n*'.format(style), '', entry[1]['content'])
    return dic


def createFormattedStylesFromClasses(dic):
    formatStyles = [None]*len(dic)
    for i, value in enumerate(dic.values()):
        classname = ' '.join(map(lambda x: '.'+x+',', value['classes']))[:-1]
        formatStyles[i] = classname + ' {'+value['content']+'};\n'
    return formatStyles


def replaceSpreadStyles(styles):
    dic = makeClassContentDic(styles)
    dic = detectClassesInContent(dic)
    return createFormattedStylesFromClasses(dic)


def removeCamelCase(inline):
    return re.sub(r'(?<!translate)([A-Z])', lambda x: '-'+x.group(0).lower(), inline)


def convertToClassName(inline):
    return re.sub(r'(?:export )*const ([a-zA-z0-9\-]+) = ', '.\\1 ', inline)


def constToCssVarFormat(const):
    return re.sub(r'_', '-', const.lower())


def formatColorsToLowercase(inline):
    return re.sub(r'(#(?:[A-Za-z0-9]{6})|#(?:[A-Za-z0-9]{3}))', lambda x: x.group(0).lower(), inline)


def templatesToCalc(style):
    return re.sub(r'(?:\$\{)([^\{\}]+)(?:\})', r"calc(\1)", style)


def inlineStylesToCss(styles, constDic):
    styles = map(templatesToCalc, styles)
    styles = map(formatColorsToLowercase, styles)
    styles = map(formatIfInlineSingleLine, styles)
    styles = map(lambda x: addCssVarsToInline(x, constDic), styles)
    styles = map(removeSpeechMarks, styles)
    styles = map(replaceCommasWithColons, styles)
    styles = replaceSpreadStyles(styles)
    styles = map(removeCamelCase, styles)
    return map(convertToClassName, styles)


def convertConstDicToCssVars(constDic):
    return map(lambda x: '--{}: {};'.format(constToCssVarFormat(x[0]), x[1]), constDic.items())


def writeToCssFile(newFileName, cssVars, styles):
    with open(os.path.join(currentpath, newFileName), 'a+') as f:
        if (len(cssVars)):
            f.write(":root {\n")
            for var in cssVars:
                f.write("    %s\n" % var)
            f.write("}\n\n")
        for style in styles:
            f.write("%s\n\n" % style)


def convertInlinesToCssFile(file, inlines, constDic):
    if (len(inlines)):
        newFileName = re.sub(r'.js', '.css', file)
        styles = inlineStylesToCss(inlines, constDic)
        cssVars = convertConstDicToCssVars(constDic)
        writeToCssFile(newFileName, cssVars, styles)


def removeUnusedConsts(read_file):
    keys = getNonExportConstants(read_file)
    for i in range(len(keys)):
        if (len(re.findall(keys[i], read_file)) < 2):
            read_file = re.sub(
                r'const {} = ([a-zA-Z0-9_\-\'\"\`]+);'.format(keys[i]), '', read_file)
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


def openFile(currentpath, file):
    path = (os.path.join(currentpath, file))
    read_file = open(path, 'r').read()
    return [path, read_file]


def convertFile(file, path, read_file):
    constants = fileConstDic(read_file)
    inlines = findInlineStylesFromCss(read_file)
    map(addInlineToConvertedList, inlines)
    constInlines = usedConstInlines(inlines, constants)
    writeToJsFile(read_file, inlines, path)
    convertInlinesToCssFile(file, inlines, constInlines)


def createImportFile(importList):
    importListFile = open(dir + '/import_list', 'w')
    for key, value in importList.items():
        if (len(value)):
            importListFile.write("import './" + key + ".css';\n")


importList = {}
dir = getDirectory()
os.system('prettier --write {}/*.js'.format(dir))
for currentpath, folders, files in os.walk(dir):
    for file in files:
        if file.endswith(".js"):
            path, read_file = openFile(currentpath, file)
            importList[file[:-3]] = []
            convertFile(file, path, read_file)
            createImportFile(importList)


styleNames = sorted(list(chain.from_iterable(importList.values())))
print(styleNames)
