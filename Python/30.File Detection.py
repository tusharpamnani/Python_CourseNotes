from genericpath import isdir, isfile
import os 

path = "C:\\Users\\LENOVO\\Desktop\\GFG" 
path2 ="C:\\Users\\LENOVO\\Desktop\\TXT.txt" 

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exists!")

if os.path.exists(path2):
    print("That location exists!")
    if os.path.isfile(path2):
        print("That is a file")
else:
    print("That location doesn't exists!")

