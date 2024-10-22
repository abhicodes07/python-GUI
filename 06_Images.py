from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Introduction to Tkinter.")

# add custom icon to the window
root.iconbitmap("A:/Studystuff/Python/python-GUI/python_icon_191765.ico")

# open images
my_img = ImageTk.PhotoImage(Image.open("A:/Screenshots/nvim.png"))
my_label = Label(image=my_img)
my_label.pack()

# quit window button
button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()
