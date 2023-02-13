# *Args = parameter that will pack all arguments into a tuple
#        Useful so that a function can accept a varying amount of arguments

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    for i in stuff:
        sum +=i
    return sum


print(add(1,2,3,4,5,6,7,8,9))