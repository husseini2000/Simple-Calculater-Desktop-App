# Importing the necessary modules
from tkinter import *
import parser
from math import factorial

root = Tk()
root.geometry('500x400')
root.title('Standard Calculator')

# It keeps the track of current position on the input text field
i = 0


# Receives the digit as parameter and display it on the input field
def get_variables(num):
    global i
    screen.insert(i, num)
    i += 1


# Calculate function scans the string to evaluates and display it
def calculate():
    entire_string = screen.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        screen.insert(0, result)
    except Exception:
        clear_all()
        screen.insert(0, "Error")


# Function which takes operator as input and displays it on the input field
def get_operation(operator):
    global i
    length = len(operator)
    screen.insert(i, operator)
    i += length


# Function to clear the input field
def clear_all():
    screen.delete(0, END)


# Function which works like backspace
def undo():
    entire_string = screen.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        screen.insert(0, new_string)
    else:
        clear_all()
        screen.insert(0, "Error")


# Function to calculate the factorial and display it
def fact():
    entire_string = screen.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        screen.insert(0, result)
    except Exception:
        clear_all()
        screen.insert(0, "Error")


# --------------------------------------UI Design ---------------------------------------------

# Set Columnconfigure & Rowconfigure for resize
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=1)
Grid.columnconfigure(root, 4, weight=1)
Grid.rowconfigure(root, 5, weight=1)
Grid.columnconfigure(root, 5, weight=1)
Grid.rowconfigure(root, 6, weight=1)

# adding the input field
screen = Entry(root)
screen.grid(row=1, columnspan=6, sticky="NSEW")

# Code to add buttons to the Calculator
Button(root, text="1", command=lambda: get_variables(1)).grid(row=2, column=0, sticky="NSEW")
Button(root, text="2", command=lambda: get_variables(2)).grid(row=2, column=1, sticky="NSEW")
Button(root, text="3", command=lambda: get_variables(3)).grid(row=2, column=2, sticky="NSEW")

Button(root, text="4", command=lambda: get_variables(4)).grid(row=3, column=0, sticky="NSEW")
Button(root, text=" 5", command=lambda: get_variables(5)).grid(row=3, column=1, sticky="NSEW")
Button(root, text=" 6", command=lambda: get_variables(6)).grid(row=3, column=2, sticky="NSEW")

Button(root, text="7", command=lambda: get_variables(7)).grid(row=4, column=0, sticky="NSEW")
Button(root, text=" 8", command=lambda: get_variables(8)).grid(row=4, column=1, sticky="NSEW")
Button(root, text=" 9", command=lambda: get_variables(9)).grid(row=4, column=2, sticky="NSEW")

# adding other buttons to the calculator
Button(root, text="AC", command=lambda: clear_all()).grid(row=5, column=0, sticky="NSEW")
Button(root, text=" 0", command=lambda: get_variables(0)).grid(row=5, column=1, sticky="NSEW")
Button(root, text=" .", command=lambda: get_variables(".")).grid(row=5, column=2, sticky="NSEW")

Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3, sticky="NSEW")
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3, sticky="NSEW")
Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3, sticky="NSEW")
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3, sticky="NSEW")

# adding new operations
Button(root, text="pi", command=lambda: get_operation("*3.14")).grid(row=2, column=4, sticky="NSEW")
Button(root, text="%", command=lambda: get_operation("%")).grid(row=3, column=4, sticky="NSEW")
Button(root, text="(", command=lambda: get_operation("(")).grid(row=4, column=4, sticky="NSEW")
Button(root, text="exp", command=lambda: get_operation("**")).grid(row=5, column=4, sticky="NSEW")

Button(root, text="<-", command=lambda: undo()).grid(row=2, column=5, sticky="NSEW")
Button(root, text="x!", command=lambda: fact()).grid(row=3, column=5, sticky="NSEW")
Button(root, text=")", command=lambda: get_operation(")")).grid(row=4, column=5, sticky="NSEW")
Button(root, text="^2", command=lambda: get_operation("**2")).grid(row=5, column=5, sticky="NSEW")
Button(root, text="^2", command=lambda: get_operation("**2")).grid(row=5, column=5, sticky="NSEW")
Button(root, text="=", command=lambda: calculate()).grid(columnspan=6, sticky="NSEW")

root.mainloop()
