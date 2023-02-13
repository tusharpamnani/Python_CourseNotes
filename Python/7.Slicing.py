#slicing = create a substring by extracting elements from another string 
#           indexing[]       or  slice()
#           [star:stop:step] or (start,stop,step)


name= "Tushar Pamnani"
first_name = name[0:4] #This will return just Tush
#starting index is inclusive whereas stopping is exclusive

first_name = name[0:6] #This will return Tushar

irst_name = name[:6] #This will return the string starting from the start

print(first_name)


last_name = name[7:14] #This will return Pamnani

last_name = name[7:] 
#this will return the string ending at the last of the original string

print(last_name)


funky_name = name[0:14:1] #By default step is taken as 1

funky_name = name[0:14:2] 
#This will return every second index of the original string

funky_name = name[0:14:3] 
#This will return every third index of the original string

funky_name = name[::3] 
#another way of writting it
#start at the beginning and end at the last of the original string

print(funky_name)


reversed_name = name[::-1] #Reverses the string 

reversed_name = name[::-2] 
#Reverses the string and returns every second index of the original string

print(reversed_name)



website1 = "https://google.com"
website2 = "https://facebook.com"

slice = slice(8,-4)


print(website1[slice])
print(website2[slice])