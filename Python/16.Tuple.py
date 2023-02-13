#Tuple = collection which is ordered and unchangable used to group  #       together related data

student = ("Tushar" , 19, "male")

print(student.count("Tushar"))
print(student.index("male"))

for x in student:
    print(x)

if "Tushar" in student:
    print("Tushar is here")