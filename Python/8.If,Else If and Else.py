#if statement = a block of code that willd execute if it's condition is true
#Here, order of the statements matter

age = int(input("How old are you?: "))

if age >=18:
    print("You are an adult")
elif age==100:
    print("You are a century old")
elif age<0:
    print("You havent been born yet")
else:
    print("You are a child")


age = int(input("How old are you?: "))
if age==100:
    print("You are a century old")
elif age >=18:
    print("You are an adult")
elif age<0:
    print("You havent been born yet")
else:
    print("You are a child")