# Method Chaining = calling multiple sequentially.
#                   each call performs an action on the same object and return self.


class Car:
    def turn_on(self):
        print("You start the engine")
        return self

    def drive (self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brake")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

#traditional method
car.turn_on()
car.drive()

#method chaining 
car.turn_on().drive() 
car.brake().turn_off()
# For this method to work we need to add return self after every function



car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
# "\" is used for line continuation
# Just to make it look good (if there are a lot of functions to call)