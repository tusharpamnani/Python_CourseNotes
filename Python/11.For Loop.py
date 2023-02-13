#for loop = a statement that will execute it's block of code for a limited
#           amount of times

#           while loop = unlimited number of times 
#           for loop = limited amount of times



for i in range(10): #starts from 0 and ends at 9 (10 is exclusive)
    print(i)

for i  in range (50, 100): #starts at 50 and ends at 99 (100 is exclusive)
    print(i)

for i in range (20,40,2):#starts at 20, ends at 39 and steps up by 2 
    print(i)

for i in "Tushar Pamnani":
    print(i)


import time 

for seconds in range (10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year")