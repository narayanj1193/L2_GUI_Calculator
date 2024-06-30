# TAKEN AND ADAPTED FROM CODE ROOM  - https://www.youtube.com/watch?v=fmMnRcrVtAE
import customtkinter
from tkinter import *
from tkinter import messagebox


# Function to update the equation in the entry field
def update_equation(value):
    current_equation = equation_entry.get()
    equation_entry.delete(0, END)
    equation_entry.insert(0, current_equation + value)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

c_app = customtkinter.CTk()
c_app.title('Calculator')
c_app.geometry('700x700')
c_app.resizable(width=False, height=False)

font1 = ('Verdana', 30, 'bold')


def button_click(number):
    equation_entry.insert(END, number)


equation_entry = customtkinter.CTkEntry(c_app, font=font1, width=650, height=90)
equation_entry.place(relx=0.5, y=50, anchor=CENTER)

# Buttons for digits and operators
b1_button = customtkinter.CTkButton(c_app, command=lambda: button_click('7'), font=font1,
                                    cursor='hand2', width=153.6, height=75,
                                    border_color='#343638', text_color='white', text='7', hover_color='#4E5051',
                                    fg_color='#9A9B9C', border_width=2)
b1_button.place(relx=0.04, rely=0.175)

b2_button = customtkinter.CTkButton(c_app, command=lambda: button_click('8'), font=font1,
                                    cursor='hand2', width=153.6, height=75,
                                    border_color='#343638', text_color='white', text='8', hover_color='#4E5051',
                                    fg_color='#9A9B9C', border_width=2)
b2_button.place(relx=0.35, rely=0.175)

b3_button = customtkinter.CTkButton(c_app, command=lambda: button_click('9'), font=font1,
                                    cursor='hand2', width=153.6, height=75,
                                    border_color='#343638', text_color='white', text='9', hover_color='#4E5051',
                                    fg_color='#9A9B9C', border_width=2)
b3_button.place(relx=0.67, rely=0.175)

b4_button = customtkinter.CTkButton(c_app, command=lambda: button_click('4'), font=font1,
                                    cursor='hand2', width=153.6, height=75,
                                    border_color='#343638', text_color='white', text='4', hover_color='#4E5051',
                                    fg_color='#9A9B9C', border_width=2)
b4_button.place(relx=0.04, rely=0.325)

b5_button = customtkinter.CTkButton(c_app, command=lambda: button_click('5'), font=font1,
                                    cursor='hand2', width=153.6, height=75,
                                    border_color='#343638', text_color='white', text='5', hover_color='#4E5051',
                                    fg_color='#9A9B9C', border_width=2)
b5_button.place(relx=0.35, rely=0.325)

b6_button = customtkinter.CTkButton(c_app, command=lambda: button_click('6'), font=font1,
                                    cursor='hand2', width=153.6, height=75,
                                    border_color='#343638', text_color='white', text='6', hover_color='#4E5051',
                                    fg_color='#9A9B9C', border_width=2)
b6_button.place(relx=0.67, rely=0.325)

b7_button = customtkinter.CTkButton(c_app, command=lambda: button_click('1'), font=font1,
                                    cursor='hand2', width=153.6, height=75,
                                    border_color='#343638', text_color='white', text='1', hover_color='#4E5051',
                                    fg_color='#9A9B9C', border_width=2)
b7_button.place(relx=0.04, rely=0.475)

b8_button = customtkinter.CTkButton(c_app, command=lambda: button_click('2'), font=font1,
                                    cursor='hand2', width=153.6, height=75,
                                    border_color='#343638', text_color='white', text='2', hover_color='#4E5051',
                                    fg_color='#9A9B9C', border_width=2)
b8_button.place(relx=0.35, rely=0.475)

b9_button = customtkinter.CTkButton(c_app, command=lambda: button_click('3'), font=font1,
                                    cursor='hand2', width=153.6, height=75,
                                    border_color='#343638', text_color='white', text='3', hover_color='#4E5051',
                                    fg_color='#9A9B9C', border_width=2)
b9_button.place(relx=0.67, rely=0.475)

b10_button = customtkinter.CTkButton(c_app, command=lambda: button_click('0'), font=font1,
                                     cursor='hand2', width=153.6, height=75,
                                     border_color='#343638', text_color='white', text='0', hover_color='#4E5051',
                                     fg_color='#9A9B9C', border_width=2)
b10_button.place(relx=0.04, rely=0.625)

b11_button = customtkinter.CTkButton(c_app, command=lambda: button_click('.'), font=font1,
                                     cursor='hand2', width=153.6, height=75,
                                     border_color='#343638', text_color='white', text='.', hover_color='#4E5051',
                                     fg_color='#9A9B9C', border_width=2)
b11_button.place(relx=0.35, rely=0.625)

c_app.mainloop()
