# walrus operator ":="

# New to Python 3.8
# assignment expression aka walrus operator
# assigns values to the variablesas a part of larger expression

happy = True    # Two lines of code 
print(happy)

print(happy := True) #Same function but in one line of code 


#Traditional method
foods = list()
while True:
    food = input("What food do you like?: ")
    if food =="quit":
        break
    foods.append(food)

foods = list()


#Walrus Operator 
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)