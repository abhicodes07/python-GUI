from tkinter import *

root = Tk()

myLable1 = Label(root, text="Hello GUI!")
myLabel2 = Label(root, text="My name is abhinav.")

myLable1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop()