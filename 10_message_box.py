from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Message Box!")

"""
Types of messagebox provided: showinfo, showerror, askquestion, askokcancel, askyesno
"""

# create messagebox
def popup():
    response = messagebox.askyesno("Hii", "Hello world!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="Clicked yes").pack()
    else:
        Label(root, text="Clicked no").pack()



Button(root, text="Popup", command=popup).pack()

root.mainloop()



