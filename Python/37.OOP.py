from Car import Car 

car_1 = Car("Chevy","Corvette",2021,"Blue")
car_2 =Car("Ford","Mustang",1967,"Black")

car_1.wheels = 2
print(car_1.wheels) #this will use the above specified value
print(car_2.wheels) #this will use the default value

#If we wanna change the default value of a class variable for this particular program

Car.wheels = 5
print(car_1.wheels) #This will still use the above specified value
print(car_2.wheels) #This will use the modified default value

car_1.drive()
car_2.stop()