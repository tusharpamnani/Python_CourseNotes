# nested functions cells = function calls inside other function calls
#                          innermost functions calls are resolved first
#                          returned value is used as argument for the next outer function


num = input("Enter a whole number: ")
num = float(num)
num = abs(num)
num = round(num)

print(num)

print(round(abs(float(input("Enter a number: ")))))