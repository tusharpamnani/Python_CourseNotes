# Module = a file containing python code.May contain functions, classes, etc.
#used with modular programming, which is to seperate a program into path

from sys import modules
import Messages #importing the module we created 
Messages.hello()
Messages.bye()


import Messages as msg #Giving the module a nickname
msg.hello()
msg.bye()


from Messages import hello,bye #importing the functions we need from the module we created
hello()
bye()


help("modules") #all the pre-written modules Python has will be displayed in the console