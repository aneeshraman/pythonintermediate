# Importing the tkinter library
from tkinter import *

# Creating the window.
root = Tk()

# Create a Label Widget.
my_label_1 = Label(root, text="Hello World!")

# Create another Label Widget.
my_label_2 = Label(root, text="My Name Is Aneesh Raman")

# Placing the first widget on screen using grid.
my_label_1.grid(row=0, column=0)

# Placing the second widget on the screen using grid.
my_label_2.grid(row=1, column=5)

# Creating the main loop.
root.mainloop()
