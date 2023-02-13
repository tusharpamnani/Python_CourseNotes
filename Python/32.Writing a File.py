text = "This Text Has Been Appended"

with open("test.txt", 'a') as file:
    file.write(text)

#'a' is used to append the file.
#'w' is used to overwrite the file

text2 = "This file has been overwritten"

with open("test.txt", 'w') as file:
    file.write(text2)