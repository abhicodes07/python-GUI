from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Imagica")
#TODO: Add Icon bitmap

my_image1 = ImageTk.PhotoImage(Image.open("A:/Grunge/Vectors/3rd division (Bleach).jpg"))
my_image2 = ImageTk.PhotoImage(Image.open("A:/Studystuff/Python/python-GUI/assets/brand of the sacrifice.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("A:/Studystuff/Python/python-GUI/assets/download (1).jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("A:/Studystuff/Python/python-GUI/assets/download.jpg"))

img_lst = [my_image1, my_image2, my_image3, my_image4]


my_label = Label(image=my_image1, width=50, height=50)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_num):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=img_lst[image_num-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_num+1))
    button_back = Button(root, text="<<", command=lambda: back(image_num-1))

    if image_num == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget() 
    my_label = Label(image=img_lst[image_num-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_num+1))
    button_back = Button(root, text="<<", command=lambda: back(image_num-1))

    if image_num == 1:
        button_back == Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

# create buttons
button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

# pack buttons
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()






