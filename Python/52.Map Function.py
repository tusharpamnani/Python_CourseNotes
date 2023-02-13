# map() = applies a function to each item in an iterable

# map(function, iterable)

store = [
    ("shirt",20.00),
    ("pant",25.00),
    ("jacket",50.00),
    ("socks",10.00)
    ]

to_euros = lambda data: (data[0],data[1]*0.82)
to_ruppees = lambda data: (data[0],data[1]*82)

store_euros = list(map(to_euros, store))
for i in store_euros:
    print(i)


store_ruppees = list(map(to_ruppees, store))
for i in store_ruppees:
    print(i)