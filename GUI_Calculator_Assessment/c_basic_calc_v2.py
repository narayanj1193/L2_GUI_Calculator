# ADAPTED FROM CODE ROOM  - https://www.youtube.com/watch?v=fmMnRcrVtAE

import customtkinter
from tkinter import *
from tkinter import messagebox


# Function to update the equation in the entry field
def update_equation(value):
    current_equation = equation_entry.get()
    equation_entry.delete(0, END)
    equation_entry.insert(0, current_equation + value)


def button_click(number):
    if len(equation_entry.get()) < 30:
        equation_entry.configure(state='normal')  # Change state to normal before updating
        current_equation = equation_entry.get()
        equation_entry.delete(0, END)
        equation_entry.insert(END, current_equation + number)
        equation_entry.configure(state='readonly')  # Change state back to readonly after updating


def key_press(event):
    if len(equation_entry.get()) < 30 or event.keysym in ['Return', 'BackSpace']:
        equation_entry.configure(state='normal')  # Change state to normal before updating
        char = event.char
        current_equation = equation_entry.get()

        if char.isdigit() or char in ['.', '+', '-', 'x', '/']:  # allow only digits and some operators
            equation_entry.delete(0, END)
            equation_entry.insert(END, current_equation + char)
        elif event.keysym == 'Return':
            calculate()
        elif event.keysym == 'BackSpace':
            current_equation = equation_entry.get()[:-1]
            equation_entry.delete(0, END)
            equation_entry.insert(0, current_equation)
        equation_entry.configure(state='readonly')  # Change state back to readonly after updating


def clear():
    equation_entry.configure(state='normal')
    equation_entry.delete(0, END)
    equation_entry.configure(state='readonly')


def calculate():
    try:
        equation = equation_entry.get()
        new_equation = equation.replace('x', '*')
        result = eval(new_equation)
        clear()
        equation_entry.configure(state='normal')
        equation_entry.insert(0, result)
    except (ZeroDivisionError, SyntaxError):
        messagebox.showerror('Syntax Error', 'Please enter a valid equation.')
    equation_entry.configure(state='readonly')


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

c_app = customtkinter.CTk()
c_app.title('Calculator')
c_app.geometry('700x700')
c_app.resizable(width=False, height=False)

font1 = ('Verdana', 30, 'bold')

equation_entry = customtkinter.CTkEntry(c_app, font=font1, width=650, height=90, state='readonly')
equation_entry.place(relx=0.5, rely=0.117, anchor=CENTER)

# Bind key press events to the key_press function
c_app.bind('<Key>', key_press)

# List of button labels and their positions
digit_buttons = [
    ('7', 0.04, 0.229), ('8', 0.272, 0.229), ('9', 0.506, 0.229),
    ('4', 0.04, 0.366), ('5', 0.272, 0.366), ('6', 0.506, 0.366),
    ('1', 0.04, 0.503), ('2', 0.272, 0.503), ('3', 0.506, 0.503),
    ('0', 0.04, 0.641), ('.', 0.272, 0.641)
]

# Create buttons using a loop
for text, relx, rely in digit_buttons:
    digit_button = customtkinter.CTkButton(c_app, command=lambda t=text: button_click(t), font=font1,
                                           cursor='hand2', width=153, height=75,
                                           border_color='#343638', text_color='white', text=text, hover_color='#3C3E3E',
                                           fg_color='#505253', border_width=2)
    digit_button.place(relx=relx, rely=rely)

# List of button labels and their positions
operator_buttons = [
    ('+', 0.739, 0.229),
    ('-', 0.739, 0.366),
    ('x', 0.739, 0.503),
    ('/', 0.739, 0.641)
]

# Create buttons using a loop
for text, relx, rely in operator_buttons:
    digit_button = customtkinter.CTkButton(c_app, command=lambda t=text: button_click(t), font=font1,
                                           cursor='hand2', width=153, height=75,
                                           border_color='#343638', text_color='white', text=text, hover_color='#887148',
                                           fg_color='#dcb575', border_width=2)
    digit_button.place(relx=relx, rely=rely)

clear_button = customtkinter.CTkButton(c_app, command=clear, font=font1, cursor='hand2', width=153, height=75,
                                       border_color='#343638', text_color='white', hover_color='#7F8081',
                                       fg_color='#9A9B9C', border_width=2, text='C')
clear_button.place(relx=0.506, rely=0.641)

equal_button = customtkinter.CTkButton(c_app, command=calculate, font=font1, cursor='hand2', width=640, height=75,
                                       border_color='#343638', text_color='white', hover_color='#887148',
                                       fg_color='#dcb575', border_width=2, text='=')
equal_button.place(relx=0.041, rely=0.778)

c_app.mainloop()
