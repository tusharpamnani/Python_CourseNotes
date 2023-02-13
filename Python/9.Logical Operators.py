#logical operators(and, or, not)= used to check if two or more conditional statements are true


temp = int(input("What is the temperature outside?: "))

if not (temp>=0 and temp<=30) :
    print("The temperature is bad today")
    print("Don't go outside")    
elif not (temp<0 or temp>30):
    print("The temperature is good today")
    print("Go outside")
