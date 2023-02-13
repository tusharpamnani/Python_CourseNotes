try:
    with open('Test.txt') as file:
        print(file.read())

except FileNotFoundError:
    print("That file wasn't found :(")

print(file.closed)