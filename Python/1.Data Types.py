#Variable = a container for a value. Behaves as the value that it contains 
#String = a series of characters. Created using '' or ""
#int = Integer value. No need of '' or ""
#float = a decimal number
#boolean = True or False

name = "Tushar"     #Here, name = variable and Bro = string
print(name)
print("Hello " + name)   #Here, we are combining 2 strings 
print(type(name))   #here, we are checking the data type of the variable name

first_name = "Tushar"
last_name = "Pamnani"
full_name = first_name + " " + last_name
print("Hello! " + full_name)

age = 18         #Here, age = integer
age = age + 1    # another way to write it is age+=1
print (age)

time = 16
time +=1 
print (time)
print(type(time))
print(type(age))


#pen = "22"  #strings cannot be used for any sort of mathematical calculation 
#pen +=1     
#print(pen)


#car = 16
#car +=1 
#print ("your car number is " + car) 
# we cannot join two different kinds of data types together, "...." is a string which cant be joined with an integer


car = 16
car +=1 
print ("your car number is " + str(car)) 
#If we want to join two different types of data types we would have to convert one into another


height = 250.55     #Here, height = Float
print(height)
print(type(height))
print("Your heightis " + str(height) + " cm" )

human = True       #Here, human = boolean
print(human)
print (type(human))
print("Are you a human : " + str(human))