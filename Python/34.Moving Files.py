import os

source = "test.txt"
destination = "C:\\Users\\LENOVO\\Desktop\\TXT.txt"

try:
    if os.path.exists(destination):
        print("There's already a file there")
    else:
        os.replace(source,destination)
        print(source+ "was moved")

except FileNotFoundError:
    print(source+"was not found")


source = "test1.txt"
destination = "C:\\Users\\LENOVO\\Desktop\\llop.txt"

try:
    if os.path.exists(destination):
        print("There's already a file there")
    else:
        os.replace(source,destination)
        print(source+ "was moved")

except FileNotFoundError:
    print(source+"was not found")