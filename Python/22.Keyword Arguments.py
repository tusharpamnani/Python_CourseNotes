#Keyword Arguments = arguments preceded by an indentifier when we pass them to a function
#                    The order of the arguments doesn't matter, untill positional arguments
#                    Python knows the names of thearguments that our function receives

def hello(first,middle,last):
    print("Hello!"+ " "+ first+ " "+ middle + " " + last)


hello("Tushar","Damn","Pamnani")
hello("Damn","Tushar","Pamnani")
hello(last = "Pamnani" , first="Tushar" ,middle = "Damn") 
#Here, first,middle and last are keywords