import os
import shutil

#Trying to remove a file

os.remove('lame.txt')
print('lame.txt was deleted')


#Trying to remove an empty folder
#This won't remove a folder with some files in it

path = 'empty_folder'

try:
    os.remove(path)
except FileNotFoundError:
    print("The fille was not found")
except PermissionError:
    print("You do not have permission to delete the folder")
#This command will not remove a folder it can only be used to delete any file

#To remove an empty folder there's an another command

try:
    os.rmdir(path)
except FileNotFoundError:
    print("The fille was not found")
except PermissionError:
    print("You do not have permission to delete the folder")
else:
    print(path + " was deleted")


#Trying to remove a folder with some files in it
source =  "folder"
try:
    os.rmdir(source)
except FileNotFoundError:
    print("The fille was not found")
except PermissionError:
    print("You do not have permission to delete the folder")
except OSError:
    print("You can not delete this folder with that function")
else:
    print(source + " was deleted")

#To delete a non-empty folder the command function used is

try:
    shutil.rmtree(source)
except FileNotFoundError:
    print("The fille was not found")
except PermissionError:
    print("You do not have permission to delete the folder")
else:
    print(source + " was deleted")
