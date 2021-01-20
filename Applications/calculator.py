# Importing the tkinter library
from tkinter import *
import keyboard

# Creating a window.
root = Tk()

# Changing the title.
root.title("Simple Calculator")

# Creating a calculator input text box.
calculator_input = Entry(root, width=35, borderwidth=5)

# Placing the calculator text box.
calculator_input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Creating function for checking for text input.

# Creating function for button 7.
def func_button_7():
    calculator_input.insert(len(calculator_input.get()) + 1, "7")


# Creating button 7.
button_7 = Button(root, text="7", padx=40, pady=20, command=func_button_7)


# Creating function for button 8.
def func_button_8():
    calculator_input.insert(len(calculator_input.get()) + 1, "8")


# Creating button 8.
button_8 = Button(root, text="8", padx=40, pady=20, command=func_button_8)


# Creating function for button 9.
def func_button_9():
    calculator_input.insert(len(calculator_input.get()) + 1, "9")


# Creating button 9.
button_9 = Button(root, text="9", padx=40, pady=20, command=func_button_9)

# Placing the buttons on screen.
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)


# Creating function for button 4.
def func_button_4():
    calculator_input.insert(len(calculator_input.get()) + 1, "4")


# Creating button 4.
button_4 = Button(root, text="4", padx=40, pady=20, command=func_button_4)


# Creating function for button 5.
def func_button_5():
    calculator_input.insert(len(calculator_input.get()) + 1, "5")


# Creating button 5.
button_5 = Button(root, text="5", padx=40, pady=20, command=func_button_5)


# Creating function for button 6.
def func_button_6():
    calculator_input.insert(len(calculator_input.get()) + 1, "6")


# Creating button 6.
button_6 = Button(root, text="6", padx=40, pady=20, command=func_button_6)

# Placing the buttons on screen.
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)


# Creating function for button 1.
def func_button_1():
    calculator_input.insert(len(calculator_input.get()) + 1, "1")


# Creating button 1.
button_1 = Button(root, text="1", padx=40, pady=20, command=func_button_1)


# Creating function for button 2.
def func_button_2():
    calculator_input.insert(len(calculator_input.get()) + 1, "2")


# Creating button 2.
button_2 = Button(root, text="2", padx=40, pady=20, command=func_button_2)


# Creating function for button 3.
def func_button_3():
    calculator_input.insert(len(calculator_input.get()) + 1, "3")


# Creating button 3.
button_3 = Button(root, text="3", padx=40, pady=20, command=func_button_3)

# Placing the buttons on screen.
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)


# Creating function for button 0.
def func_button_0():
    calculator_input.insert(len(calculator_input.get()) + 1, "0")


# Creating button 0.
button_0 = Button(root, text="0", padx=40, pady=20, command=func_button_0)


def func_button_clear():
    calculator_input.delete(0, END)


# Creating button clear.
button_clear = Button(root, text="Clear", padx=77, pady=20, command=func_button_clear)

# Placing the buttons on screen.
button_0.grid(row=4, column=0)
button_clear.grid(columnspan=2, row=4, column=1)


# Creating a function for button +.
def func_button_plus():
    calculator_input.insert(len(calculator_input.get()) + 1, "+")


# Creating button +.
button_plus = Button(root, text="+", padx=40, pady=20, command=func_button_plus)


# Creating a function for button =.
def func_button_equals():
    if "+" in calculator_input.get():
        try:
            return int(calculator_input[:calculator_input.get().index("+")]) + int(
                calculator_input[calculator_input.get().index("+") + 1:])

        except ValueError:
            func_button_clear()
            calculator_input.insert(0, "Wrong Input")


    elif "-" in calculator_input.get():
        try:
            return int(calculator_input[:calculator_input.get().index("-")]) + int(
                calculator_input[calculator_input.get().index("-")+1:])

        except ValueError:
            func_button_clear()
            calculator_input.insert(0, "Wrong Input")


# Creating button =
button_equals = Button(root, text="=", padx=86.5, pady=20)

# Placing the buttons on screen.
button_plus.grid(row=5, column=0)
button_equals.grid(columnspan=2, row=5, column=1)

# Creating button -.
button_minus = Button(root, text="-", padx=40, pady=20)

# Creating button *.
button_star = Button(root, text="*", padx=40, pady=20)

# Creating button /.
button_divide = Button(root, text="/", padx=40, pady=20)

# Creating the mainloop.
root.mainloop()
