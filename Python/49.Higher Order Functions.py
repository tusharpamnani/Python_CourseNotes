# Higher Order Functions = a functionn that either :
#                          1. accepts a function as an argument
#                                   or
#                          2. returns a function 
#                           (In Python, functions are also treated as objects)


def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func): #This is an example of 1st type of Higher Order Function (accepts a function as an argument)
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)


def divisor(x): # This is an example of 2nd type of Higher Order Function (returns a function)
    def dividend(y):
        return y/x 
    return dividend


divide = divisor(2)
print(divide(42))

# First we called divisor as 2. since we didn't call dividend, therefore the computer scipped  "def dividend(y): return y/x" and carried on with the "return dividend" part.
# Then the program went on to the dividend part where we assigned it 42. Then the program went on with the remaining part that is "return y/x" ad divided 42 by 2.
# This finally gave the aanswer at the terminal, 21.0

