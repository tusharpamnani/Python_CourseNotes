def hello():
    print("Hello!")

print(hello) #This will print the hexadecimal address of the fuction hello at this computer. Also,  this will change every time we run this program. 
hi = hello
print(hi) #This will print the same address as of hello


hello()
hi() # Both hello and hi wil act as a single function with different names because both have the same memory address.


say = print
say("Whoa! I can't believe this works! :O")
# This is an example for the same.