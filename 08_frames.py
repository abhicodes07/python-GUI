from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Introduction to tkinter module.")

# create a frame
frame = LabelFrame(root, text="This is a frame.", padx=50, pady=50) #padding inside the frame
frame.pack(padx=100, pady=100) # padding outside frame 

# put the buttons in a frame
b = Button(frame, text="Don't put it here!")
b2 = Button(frame, text="Heyy!")

b.grid(row=0, column=0, padx=5, pady=5)
b2.grid(row=0, column=1, padx=5, pady=5)

# main
root.mainloop()

