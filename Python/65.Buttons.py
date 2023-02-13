# button = you click it, it does stuff

from tkinter import * 

count = 0
def click():
    global count
    count+=1
    print("You clicked me")
    print(count)
window = Tk()

photo = PhotoImage(file="1666790142401.png")


button = Button(
    window,
    text="Touch Me!!",                  # Text you wanna display on the button
    command=click,                      # This is  known as a callback
    font=("Cominc Sans",30),             
    fg= "#00ff00",                      # Whenever you click the button the color scheme changes this is because there is a different active foreground and active background
    bg="black",                 
    activeforeground="#00ff00",         # This will change the active foreground 
    activebackground="black",           # This will change the active background    
    #state=DISABLED                      # This stops the button to function. This will also change the color scheme
    state=ACTIVE,
    image= photo,
    compound="right"
)         


button.pack()


window.mainloop()


