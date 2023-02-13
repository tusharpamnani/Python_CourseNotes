#   Dictionary Comphrehension = create dictionaries using an expression
#                               can  replace "for" loops and certain lambda functions 

# Dictionary = {key: expression for (key,value) in iterable}
# Dictionary = {key: expression for (key,value) in iterable if conditional}
# Dictionary = {key: if/else for (key,value) in iterable}

#-----------------------------------------------------------------------------------------

cities_in_F = {'New York':32, 'Boston':75, 'Los Angeles':109, 'Chicago':50}                         # Dictionary = {key: expression for (key,value) in iterable}

cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

#-----------------------------------------------------------------------------------------

weather = {'New York':"snowing",'Boston':"sunny",'Los Angeles':"sunny",'Chicago':"cloudy"}          # Dictionary = {key: expression for (key,value) in iterable if conditional}
sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
print(sunny_weather)

#-----------------------------------------------------------------------------------------

cities = {'New York':32, 'Boston':75, 'Los Angeles':109, 'Chicago':50}                              # Dictionary = {key: if/else for (key,value) in iterable}
desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
print(desc_cities)

#-----------------------------------------------------------------------------------------

def check_temp(value):                                                                              # Dictionary = {key: if/else for (key,value) in iterable}
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {'New York':32, 'Boston':75, 'Los Angeles':109, 'Chicago':50}
desc_cities0 = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities0)