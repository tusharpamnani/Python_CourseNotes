# zip(*iterables) = will aggregate elements from two or more iterables 
#                   creates a zip object with paired elements stored in tuples for each element



username = ["Dude","Bro","Mister"]
passwords = ("password","abc123","guest")

users = zip(username,passwords)                 # This can be typecasted to any iterable
for i in users:
    print(i)

print(type(users))

users = dict(zip(username,passwords))                # This is typecasted to dictionary
for key,value in users.items():
    print(key+" : "+value)

username = ["Dude","Bro","Mister"]
passwords = ("password","abc123","guest")
login_date = ["1/2/2020","1/2/2021","1/2/2022"]

users = zip(username,passwords,login_date)
for i in users:
    print(i)