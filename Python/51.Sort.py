# sort() method = used with lists ONLY (won't work with any other iterable)
# sort() function = used with iterables (incl. list)

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

students.sort()
for i in students:
    print(i)    #This will sort the list in the alphabetical order


students.sort(reverse=True)
for i in students:
    print(i)    #This will sort the list in the reversed alphabetical order


sorted_students = sorted(students) # This will return a list and accepts any type of iterable
for i in sorted_students:
    print(i)            #This will sort the list in the alphabetical order


sorted_students = sorted(students,reverse=True)
for i in sorted_students:
    print(i)            #This will sort the list in the reversed alphabetical order


teachers = [
    ("Squidward", "F",60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongebob", "B", 29),
    ("Mr. Krabs", "C", 78)
    ]

teachers.sort() # This list is sorted on the basis of the names (alphabetically)
for i in teachers:
    print(i)

grade = lambda grades:grades[1] # This list is sorted on the basis of the grades (which basically, have the index of 1 in the pre-defined-list)(this too, alphabetically)
teachers.sort(key=grade)
for i in teachers:
    print(i)


teachers.sort(key=grade,reverse=True)  # This list is sorted on the basis of the grades (which basically, have the index of 1in the pre-defined-list)(reversed-alphabetically)
for i in teachers:
    print(i)


age = lambda ages:ages[2] # This list is sorted on the basis of the age (which basically, have the index of 2 in the pre-defined-list)(numerically)
teachers.sort(key=age)
for i in teachers:
    print(i)

teachers.sort(key=age,reverse=True)  # This list is sorted on the basis of the ages (which basically, have the index of 1in the pre-defined-list)(reversed-numerically)
for i in teachers:
    print(i)

#   EXAMPLE FOR ANOTHER ITERABLE, TUPLE
characters = (
    ("Squidward", "F",60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongebob", "B", 29),
    ("Mr. Krabs", "C", 78)
)

age = lambda ages:ages[2]
sorted_characters = sorted(characters, key =age)
for i in sorted_characters:
    print(i)

#   Not gonna repeat everything for tuples