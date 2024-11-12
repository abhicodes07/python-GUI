from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Radio Frames.")

# tkinter variable 
r = IntVar()
r.set(2) # setting the value

def clicked(value):
    myLabel1 = Label(root, text=value)
    myLabel1.pack()

# create a radio button
rbutton1  = Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:clicked(r.get()))
rbutton2  = Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda:clicked(r.get()))

myLabel1 = Label(root, text=r.get()) # .get method to get the value(display it) / getting the value

myButton = Button(root, text="Click Here!", command=lambda: clicked(r.get()))

# pack buttons
rbutton1.pack()
rbutton2.pack()

myLabel1.pack()

myButton.pack()

root.mainloop()




