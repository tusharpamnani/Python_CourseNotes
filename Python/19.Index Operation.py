#Index Operation [] = gives access to a sequence's elements (str, list,tuples)



name = "tushar Pamnani!"

if (name[0].islower):
    name = name.capitalize()

first_name = name[:6].upper()
last_name = name[7:].lower()
last_character =  name[-1]



print(name)
print(first_name)
print(last_name)
print(last_character)