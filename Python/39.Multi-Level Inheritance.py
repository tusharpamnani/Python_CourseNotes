# Multi-Level Inheritance = when a derived (child) class inherits another derived (child) class

class organism:

    alive = True

class Animal(organism):
    def eat(self):
        print("This animal is eating")


class Dog(Animal):
    def bark(self):
        print("This dog is barking")


dog = Dog()
print(dog.alive)
dog.eat()