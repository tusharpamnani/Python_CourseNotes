# label = an areal widget that holds text and/or an image within a window

from ast import Raise
from email.mime import image
from tkinter import *
from tkinter.font import BOLD

window = Tk()

photo = PhotoImage(file='C:\\Users\\LENOVO\Desktop\\1666687491829.png')
label = Label(                                  # Creates the Label
    window,                                     # This is the master
    text="Hello Nigga!!",                       # Type of lable we need as well as the content
    font=('Arial',40,BOLD),                     # Changes the font
    fg='#00ff00',                               # Changes the forground color
    bg='black',                                 # Changes the background color
    relief=RAISED,                              # Changes the border
    bd=10,                                      # Changes the border width
    padx=25,                                    # Adds the padding wrt x axis
    pady=50,                                    # Adds the padding wrt y axis  
    image=photo,                                # Adds an image to the window
    compound='bottom')                          # Specifies where the image is to be placed
label.pack()                                    # This is to deploy the label in the GUI
# label.place(x=0,y=0)                            # Using the coordinates, lable can be placed anywhere in the window

window.mainloop()



# By default the pack() option will add the label to the top-center of the Window
# fg means ForeGround
# bg means BackGround
# Label will take up as much the space as it needs