# Importing the necessary modules
from tkinter import *
from math import factorial

root = Tk()
root.geometry('500x400')
root.title('Standard Calculator')

# It keeps track of the current position on the input text field
i = 0

# Receives the digit as a parameter and displays it on the input field
def get_variables(num):
    global i
    screen.insert(i, num)
    i += 1

# Calculate function scans the string to evaluate and display it
def calculate():
    entire_string = screen.get()
    try:
        result = eval(entire_string)
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

# Adding the input field
screen = Entry(root)
screen.grid(row=1, columnspan=6, sticky="NSEW")

# Number buttons
buttons = [
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2),
    ('0', 5, 1), ('.', 5, 2)
]
for (text, row, col) in buttons:
    Button(root, text=text, command=lambda t=text: get_variables(t)).grid(row=row, column=col, sticky="NSEW")

# Operator buttons
operations = [
    ('+', 2, 3), ('-', 3, 3), ('*', 4, 3), ('/', 5, 3),
    ('pi', 2, 4, '*3.14'), ('%', 3, 4), ('(', 4, 4), ('exp', 5, 4, '**'),
    ('<-', 2, 5, 'undo'), ('x!', 3, 5, 'fact'), (')', 4, 5), ('^2', 5, 5, '**2')
]
for op in operations:
    text, row, col = op[:3]
    command = get_operation if len(op) == 3 else (undo if op[3] == 'undo' else fact)
    Button(root, text=text, command=lambda t=text: command(t) if command != undo and command != fact else command()).grid(row=row, column=col, sticky="NSEW")

# Special buttons
Button(root, text="AC", command=clear_all).grid(row=5, column=0, sticky="NSEW")
Button(root, text="=", command=calculate).grid(columnspan=6, sticky="NSEW")

root.mainloop()
