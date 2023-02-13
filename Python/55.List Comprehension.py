# List  Comprehension = a way to create a new list with less syntax
#                       can mimic certain lambda functions,  easier to read
#                       list  = [expression for item in iterable]
#                       list  = [expression for item in iterable if conditional]
#                       list  = [expression if/else for item in iterable]



#       TRADITIONAL METHOD
squares = []                                                        #create an empty list
for i in range(1,11):                                               #create a for loop
    squares.append(i*i)                                             #define what each loop iteration should do
print (squares)

#       LIST COMPREHENSION METHOD
squares2 = [i * i for i in range(1,11)]                             #list  = [expression for item in iterable]
print(squares2)



students = [100,90,80,70,60,50,40,30,0]

passed_students = list(filter(lambda x:x >=60, students))           #can mimic certain lambda functions,  easier to read
passed_students = [i for i in students if i >=60]                   #list  = [expression for item in iterable if conditional]
passed_students =[i if i>=60 else "Failed" for i in students]       #list  = [expression if/else for item in iterable]

print(passed_students)