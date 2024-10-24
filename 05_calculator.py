from tkinter import *

root = Tk()
root.title("Calculator")

# create entry field
e = Entry(root, width=55, borderwidth=10)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# command
def Click(num):
    initial = e.get()
    e.delete(0, END)
    e.insert(0, str(initial) + str(num))

def Clear():
    e.delete(0, END)

def Add():
    f_num = e.get()
    global final
    global check
    check = "add"
    final = int(f_num) 
    e.delete(0, END)

def Mul():
    f_num = e.get()
    global final
    global check
    check = "mul"
    final = int(f_num) 
    e.delete(0, END)

def Sub():
    f_num = e.get()
    global final
    global check
    check = "sub"
    final = int(f_num) 
    e.delete(0, END)

def Equal():
    s_num = e.get()
    e.delete(0, END)

    match check:
        case "add":
            e.insert(0, final + int(s_num))
        case "sub":
            e.insert(0, final - int(s_num))
        case "mul":
            e.insert(0, final * int(s_num))
# Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: Click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: Click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: Click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: Click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: Click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: Click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: Click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: Click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: Click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: Click(0))

# operations
button_clear = Button(root, text="C", padx=40, pady=20, command=Clear) 
button_equal = Button(root, text="=", padx=88, pady=20, command=Equal) 
button_add = Button(root, text="+", padx=40, pady=20, command=Add) 
button_sub = Button(root, text="-", padx=40, pady=20, command=Sub) 
button_mul = Button(root, text="x", padx=40, pady=20, command=Mul) 

# display buttons 
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=1, column=3)
button_add.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_mul.grid(row=4, column=3)
button_equal.grid(row=4, column=1, columnspan=2)

# main
root.mainloop()