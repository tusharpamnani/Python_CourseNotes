# copyfile() = copies content of the file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)


import shutil

shutil.copyfile('test.txt','copy.txt') #source,destination 
#destination is in the project folderr that's why no need to mention the path
#copy.txt if doesn't exist, will be created automatically

shutil.copyfile('test.txt' , 'C:\\Users\\LENOVO\\Desktop\\TXT.txt')
#destination is not in the project folder that's why path has to be specified

#copy() and copy2() both will have the same arguments as copyfile()