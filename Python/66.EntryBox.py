from tkinter import *
from turtle import left, right 

# entry widget = textbox that accepts a single line of user input


def submit():
    username=entry.get()
    print("Hello "+ username + " !!")
    entry.config(state=DISABLED) #after clicking on submit, the box gets disabled

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(
    window,
    font=("sans-serif",50),
    fg="#00ff00", #foreground color of the entrybox
    bg="black", #background color of the entrybox
    show="*") #Shows the "*" for each character we insert
entry.insert(0,"Spongebob") #inserts the default text at the position (here, 0) 
entry.pack(side=LEFT) #position of the box

submit_button = Button(window,text="Submit",command= submit)
submit_button.pack(side = RIGHT) #position of thre button

delete_button = Button(window,text="Delete",command= delete)
delete_button.pack(side = RIGHT) #position of thre button

backspace_button = Button(window,text="Backspace",command= backspace)
backspace_button.pack(side = RIGHT) #position of thre button


window.mainloop()