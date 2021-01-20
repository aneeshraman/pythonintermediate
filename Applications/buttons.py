# Importing the tkinter library
from tkinter import *

# Creating the window.
root = Tk()


# Creating a function for my_button.
def my_click():
    my_label = Label(root, text="Look! The button is being clicked!!")
    my_label.pack()


# Creating a button. We can set the state of the button also.
# To change the size of a button we can use padx to change the x value and pady to change the y value.
# Hex codes can also be used in fg and bg.
my_button = Button(root, text="Click Me!", command=my_click, fg="blue", bg='red')

# Putting the button on screen.
my_button.pack()

# Creating the main loop.
root.mainloop()
