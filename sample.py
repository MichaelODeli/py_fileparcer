import fileparcer as flp
# KNOWN BUG - files and files with dot at start (sample - .vscode or .minecraft) will be counted as file. I don`t know how to fix it

# Sample One. This function male list of files with your extension, here - py. Write only one word without dot!
a=flp.fileext('py')
print(a)

# Sample Two. This function make same that previous, but in your directory. Please check, that yor dir ends with '//' sybol (tested on Windows)
# flp.fileext_dir(extension, way to files, show directories in output (true, false))
b=flp.fileext_dir('exe', r'C://Windows//', False) # without dirs
b=flp.fileext_dir('exe', r'C://Windows//', True) # with dirs
print(b)

# Sample Three. Show list of files in program root directory
c=flp.getlist()
print(c)

# Sample Four. This function check file existing.
d=flp.isfileexist('sample.py')
print(d)

# sample five. file counter
e=flp.filecounter()
print(e)

# sample six. file counter with your extension
f=flp.filecounter_ext('py')
print(f)