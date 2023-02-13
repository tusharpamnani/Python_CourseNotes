# Scope = The region that a variab;e is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped versions of a variable can be created 

name = "Tushar"         #global scope (available inside and outside functions)

def display_name():
    name = "Pamnani"    #local scope (available only inside this function)
    print(name)


display_name()
print(name)



#                                   Python Follows 
#               L = Local
#               E = Enclosing
#               G = Global
#               B = Built-in
#                                   Rule for order of variables