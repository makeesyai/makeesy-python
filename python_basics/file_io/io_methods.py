# File Types in Python
# 1. Text file
# 2. Binary file
# 3. Raw Binary file (typically not used)

# modes:
# r (default): open for reading
# r+: open for reading and writing
# w: open for writing, creates file if not there, if there truncates it
# w+: open for reading and writing, creates file if not there, if there truncates it
# a: open for writing, creates file if not there, if there places the pointer at the end of the file
# a+: open for reading and writing, creates file if not there,
# if there place the pointer at the end of the file

# filetypes: binary: b, text: t (default)

filein = open('test1.txt', mode='a+')
# print(type(filein.read()))
# print(type(filein.readline()))
# print(filein.readlines())
filein.seek(0)
for line in filein:
    print(line)
    print(type(line))
    print(list(line))

text = "Add this text to the file.\n"
filein.write(text)

filein.close()









# Tips
# NEW LINE
# WINDOWS: Carriage Return (CR or \r) and the Line Feed (LF or \n) characters (CR+LF or \r\n)
# LINUX and MAC: Line Feed (LF or \n)
# Character Encodings
# ASCII: 128 characters
# Unicode: 1,114,112 characters
