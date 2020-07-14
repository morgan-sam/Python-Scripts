import os, re
 
for currentpath, folders, files in os.walk('.'):
    for file in files:
        path = (os.path.join(currentpath, file))
	open_file = open(path,'r')
        read_file = open_file.read()
        regex = re.compile('function\ *([a-zA-Z]+) *\(([a-zA-Z, ]*)\)')
        read_file = regex.sub('const \\1 = (\\2) =>', read_file)
        write_file = open(path,'w')
        write_file.write(read_file)

for currentpath, folders, files in os.walk('.'):
    for file in files:
        path = (os.path.join(currentpath, file))
	open_file = open(path,'r')
        read_file = open_file.read()
        regex = re.compile('async *const *([a-zA-Z]+) *= *\(([a-zA-Z]*)\) *\=\> *')
        read_file = regex.sub('const \\1 = async (\\2) =>', read_file)
        write_file = open(path,'w')
        write_file.write(read_file)


