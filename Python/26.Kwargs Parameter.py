# **Kwargs = Parameter that will pack all arguments into dictionary
#            Useful so that a function can accept a varying amount of keyword argumnets 


def hello(**names):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key,value in names.items():
        print(value,end=" ")



hello(first= "Tushar", middle= "Damn", last="Pamnani")