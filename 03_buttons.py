from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look i clicked")
    myLabel.pack()

# state=DISABLED @to disable the state
# padx=integer @change size
# pady=integer @change size
# command=function_name @add the functionality to the button
#                       @we do not use paranthesis while calling 
#                        function in tkinter label 

myButton = Button(root, 
                  text="Click Me!", 
                  padx=5, 
                  pady=10, 
                  command=myClick,
                  fg="blue", # foreground color, cal also use color codes
                  bg="cyan" # background color
                )

myButton.grid(row=0, column=0)
myButton.pack()

root.mainloop()