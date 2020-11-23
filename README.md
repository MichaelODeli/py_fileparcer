# py_fileparcer
### KNOWN BUG - files and files with dot at start (sample - .vscode or .minecraft) will be counted as file. I don't know how to fix it
First - you must download fileparcer.py in your program directory and import it by command:
`import fileparcer as flp`

#### Sample One. This function male list of files with your extension, here - py. Write only one word without dot!
```
a=flp.fileext('py')
print(a)
```
#### Sample Two. This function make same that previous, but in your directory. Please check, that yor dir ends with '//' sybol (tested on Windows)
###### flp.fileext_dir(extension, way to files, show directories in output (true, false))
```
b=flp.fileext_dir('exe', r'C://Windows//', False) # without dirs
b=flp.fileext_dir('exe', r'C://Windows//', True) # with dirs
print(b)
```
#### Sample Three. Show list of files in program root directory
```
c=flp.getlist()
print(c)
```
#### Sample Four. This function check file existing.
```
d=flp.isfileexist('sample.py')
print(d)
```
#### Sample five. File counter
```
e=flp.filecounter()
print(e)
```
#### Sample six. file counter with your extension
```
f=flp.filecounter_ext('py')
print(f)
```
