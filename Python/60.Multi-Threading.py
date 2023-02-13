# thread = a flow of execution. Like a seperate order of instructions.
#              However, each thread takes a turnn running to achieve concurrency
#              GIL = global interpreter lock
#              allows omnly one thread to hold the control of the Python Interpreter 

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#              use multi-processing 

# io bound = program/task spends most of it's time waiting for external events (user input,web-scraping)
#              use multi-threading

import threading
import time
from tkinter import Y

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You study")

#eat_breakfast()
#drink_coffee()
#study()

x = threading.Thread(target = eat_breakfast)
x.start()

y = threading.Thread(target = drink_coffee)
y.start()

z = threading.Thread(target = study)
z.start()

x.join()                        # The main thread will have to wait for the thread"x" to finish so as to complete it's own set of instructions
y.join()
z.join()
print(threading.active_count()) # This will return the number of active threads running in background  
print(threading.enumerate())    # This will return the list of all the threads running in the background
#                                 The thread which is in-charge of running the program is called the "MainThread"
print(time.perf_counter())      # This will return how long it takes our calling thread as in our main thread to finish it's set of instructions