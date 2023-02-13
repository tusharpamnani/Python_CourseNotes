#------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                       If __name__ == '__main__'

#------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                               Why tho?
#                                           1. Module can be run as a standalone program
#                                           2. Module can be imported and used by other modules

#------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                              Python interpreter sets "special variables", one of whch is __name__
#                          Python will asign the __name__ variable a value of '__main__' if it's the initial module being run

#------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    print("Hello!")


if __name__ == '__main__':
    main()


#If we import this module to another module and then run this program. Then this program will run indirectly
# Basically, this program gives flexibility to the programmer    