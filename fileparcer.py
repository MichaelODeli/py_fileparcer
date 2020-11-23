# this is module file. You can see FaQ an How-to-Use on my GitHub pag. Link - 
import glob
import fnmatch
import os


def getlist():
    list=[]
    listOfFiles = os.listdir()  
    pattern = "*.*"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            list.append(entry)
    return list
def filecounter():
    list=[]
    listOfFiles = os.listdir()  
    pattern = "*.*"  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            list.append(entry)
    return len(list)
def filecounter_ext(extension):
    list=[]
    listOfFiles = os.listdir()  
    pattern = "*."+str(extension)  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
            list.append(entry)
    return len(list)
def isfileexist(filename):
    list=getlist()
    for thisfile in list:
        if thisfile==filename:
            result=1
    if result==1:
        return True
    else:
        return False
def fileext(extension): # without dot. sample - py, exe, etc
    ext='*.'+str(extension)
    mass=glob.glob(ext)
    i=0
    while i!=len(mass):
        mass[i]=mass[i].replace('\\', '/')
        i+=1
    return mass
def fileext_dir(extension, dir, ask): # without dot. sample - py, exe, etc
    dirext=str(dir)+'*.'+str(extension)
    mass=glob.glob(dirext)
    i=0
    while i!=len(mass):
        mass[i]=mass[i].replace('//', '/')
        mass[i]=mass[i].replace('\\', '/')
        i+=1
    if ask==True:
        return mass
    if ask==False:
        n=0
        dir=dir.replace('//', '/')
        dir=dir.replace('\\', '/')
        while n!=len(mass):
            mass[n]=mass[n].replace(dir, '')
            n+=1
        return mass