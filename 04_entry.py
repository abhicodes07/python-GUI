from tkinter import *

root = Tk()

# create an entry box
entry_box = Entry(root, width=20, bg="Blue")
entry_box.pack()
# put default text inside of a text box
entry_box.insert(0, "Enter you name: ",)

# what happens when you click the button you created?
def Click():
    hello = "Hello " + entry_box.get() # method to return the text from the entry box
    myLabel = Label(root, text=hello)
    myLabel.pack()

buttons = Button(root, text="Go", fg="blue", bg="orange", command=Click)
buttons.pack()

# main
root.mainloop()


