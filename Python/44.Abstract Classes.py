#Prevents a user from creating an object of that class
#compels a user to override yhe abstract methods in a child class

# Abstract class = a class which contains one or more abstract methods.
# Abstract methods = a method that has a declaration but does not have an implementation


from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):   #If any of the methods is not overriden in any of the child class of vehicle then a TypeError will appear.
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("This motorcycle is stopped")


#vehicle = Vehicle()    #Since Vehicle is an abstract class vehicle object can not be created. 
car = Car()
motorcycle = Motorcycle()


#vehicle.go() #This will give arise to an error
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()