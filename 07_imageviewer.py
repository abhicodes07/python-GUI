from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Imagica")
#TODO: Add Icon bitmap

my_image1 = ImageTk.PhotoImage(Image.open("A:/Grunge/Vectors/3rd division (Bleach).jpg"))
img_lst = [my_image1]

my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)

# create buttons
button_back = Button(root, text="<<")
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>")

# pack buttons
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()






