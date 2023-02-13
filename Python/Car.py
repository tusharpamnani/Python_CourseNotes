class Car:

    wheels = 4                  #class variable. This value will be kept as defaults value

    def __init__(self,make,model,year,color): #__init__ is known as constructor
        self.make = make        #instance variable
        self.model = model      #instance variable
        self.year = year        #instance variable
        self.color = color      #instance variable
    
   
    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")