# Importing the tkinter library
from tkinter import *

# Creating the window.
root = Tk()

# Creating a text box. To change the width use width parameter.
# To have shadow effect use borderwidth.
e = Entry(root, width=50)

# Placing the text box.
e.pack()

# Entering default text.
e.insert(0, "Name")


# Creating a function for my_button.
def my_click():
    my_label = Label(root, text=f"Hello {e.get()}")
    my_label.pack()


# Creating a button. We can set the state of the button also.
# To change the size of a button we can use padx to change the x value and pady to change the y value.
# Hex codes can also be used in fg and bg.
my_button = Button(root, text="Enter your Name", command=my_click)

# Putting the button on screen.
my_button.pack()

# Creating the main loop.
root.mainloop()
