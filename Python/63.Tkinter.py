# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain widgets

from tkinter import * 

window = Tk()                           # instantiate an instance of a window 
window.geometry("420x420")              # changes the height and width of the window THIS SHOULD ALWAYS BE WITHIN QUOTES
window.title("My First GUI")            # changes the title of the window

icon = PhotoImage(file='ass.png')       # PhototImage accepts only .png files
window.iconphoto(True, icon)            # changes the icon at the top left corner
window.config(background="green")       # changes the background color. Accepts both color name and hex-decimal value



window.mainloop()                       # place window on computer screen, listen for events             