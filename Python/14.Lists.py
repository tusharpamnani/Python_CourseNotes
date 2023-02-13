#Lists = used to store multiple items in a single variable

food = ["pizza", "hamburgers", "hot-dog"]
food[0] = "sushi"

print(food[0])

food.append("Ice-Cream") #Adds a value at the end of the existing list
food.remove("hot-dog") #Removes a specified value from the list
food.pop() #Removes the value at the end of the list
food.insert(0, "cake") #Adds the value to the specified index 
food.sort() #Sorts the list aplhabetically
food.clear() #Clears the whole list


for x in food:
    print(x)