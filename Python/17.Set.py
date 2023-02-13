#Set = collection which is unordered, unindexed, no duplicate values

from urllib.request import urlretrieve


utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("spoon")
#utensils.clear()
#utensils.update(dishes)
#dishes.update(utensils)


print(utensils.difference(dishes))

print(utensils.intersection(dishes))

dinner_table = utensils.union(dishes)


#for x in dinner_table :
#   print(x)

