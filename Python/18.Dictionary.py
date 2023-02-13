#dictionary = A changable, unordered collection of unique key:value pairs 
#             Fast because they use hashing, allow us to access a value quickly 

capitals = {'USA':'Washington DC', 'India' : 'Delhi', 'China' : 'Beijing', 'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.pop('China')
#capitals.clear()


print(capitals)
print(capitals.keys())
print(capitals.values())
print(capitals.items())


for key,value in capitals.items():
    print(key,value)