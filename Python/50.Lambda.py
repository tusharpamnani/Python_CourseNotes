# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression
#                   (think of it as a shortcut)
#                   (useful if neede for a short period of time, throw-away)
# lambda parameter(s):expression

#   Traditional method
def double(x):
    return x*2

print(double(5))

#   Using lambda function
double = lambda x: x*2
multiply = lambda x,y : x*y
add = lambda x,y,z: x+y+z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age: True if age >=18 else False

print(double(10))
print(multiply(15,2))
print(add(1,2,3))
print(full_name("Tushar","Pamnani"))
print(age_check(19))