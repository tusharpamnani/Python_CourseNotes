# daemon threading = a thread that runs in the background, not important for program to run 
#                    your program will not wait for daemon threads to complete before exiting 
#                    non daemon threads cannot normally br killed, stay alive untill task is complete

#                    ex. background tasks, ggarbage collection, waiting for input, long running processes


from itertools import count
import time
import threading

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count +=1
        print("Logged in for: ", count , "seconds")

x = threading.Thread(target = timer , daemon=True)      # If daemon = True then the timer will stop when we end the task. Else the timer will go on even after the non-daemon task is finished
x.start()

answer = input("Do you wish to exit??")