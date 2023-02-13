# Format = option available to strings
#          an optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)

print("The {} jumped over the {}".format(animal,item))
print("The {} jumped over the {}".format(item,animal))
print("The {0} jumped over the {1}".format(animal,item))
print("The {1} jumped over the {1}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item))
print("The {animal} jumped over the {item}".format(animal="cow",item ="moon"))
print("The {item} jumped over the {animal}".format(animal="cow",item ="moon"))
print("The {animal} jumped over the {animal}".format(animal="cow",item ="moon"))


text = "The {} jumped over the {}"
print(text.format("cat","moon"))
print(text.format(animal, item))


name = "Tushar"
print("Hello,my name is {}".format(name))
print("Hello,my name is {:10}.Nice to meet you".format(name))
print("Hello,my name is {:<10}.Nice to meet you".format(name)) #Left Align
print("Hello,my name is {:>10}.Nice to meet you".format(name)) #Right Align
print("Hello,my name is {:^10}.Nice to meet you".format(name)) #Center Align



number = 10202
print("The number pi is {:.2f}".format(number)) #displays first 2 decimal places and will roubd it off
print("The number pi is {:,}".format(number)) #Adds a comma after the thousands place
print("The number pi is {:b}".format(number)) #Displays the number in binary format
print("The number pi is {:o}".format(number)) #Displays the number in octet format
print("The number pi is {:X}".format(number)) #Uppercase
print("The number pi is {:x}".format(number)) #Lowercase
print("The number pi is {:e}".format(number)) #Displays the number exponentially in lowercase
print("The number pi is {:E}".format(number)) #Displays the number exponentially in upper case