from tkinter import *

window = Tk()
x = IntVar()                         # We are keeping onvalue / offvalue as an integer
#                                    x = StringVar is used when we keep onvalue / offvalue as a string value
#                                    x = booleanVar is used when we keep onvalue / offvalue as a boolean value


def display():
    if (x.get()==1):
        print("You agree!!")
    else :
        print("You don't agree :(")

photo = PhotoImage(file='ass.png')

check_button = Checkbutton(
    window,
    text="I agree to something!",
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display,
    font=("Arial",25),
    fg="#00ff00",
    bg="black",
    activebackground="black",
    activeforeground="#00ff00",
    padx=25,
    pady=10,
    image= photo,
    compound='left'                  # position where we wish to keep our image in the GUI
    )

check_button.pack()

window.mainloop()