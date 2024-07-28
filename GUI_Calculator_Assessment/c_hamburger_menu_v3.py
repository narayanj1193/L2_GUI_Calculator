import customtkinter
from tkinter import *


def toggle_menu():
    if menu_frame.winfo_viewable():
        menu_frame.place_forget()
    else:
        menu_frame.place(relx=-0.01, rely=-0.02, relwidth=0.302, relheight=1.03)


def menu_item1_click(font):
    toggle_menu()

    # Clear the window
    for widget in c_app.winfo_children():
        if widget == hamburger_button or widget == menu_frame:
            pass
        else:
            widget.destroy()

    # Display the text
    text_label = customtkinter.CTkLabel(c_app, text="This is menu item 1", font=font)
    text_label.place(relx=0.5, rely=0.5, anchor='center')


def menu_item2_click(font):
    toggle_menu()

    # Clear the window
    for widget in c_app.winfo_children():
        if widget == hamburger_button or widget == menu_frame:
            pass
        else:
            widget.destroy()

    # Display the text
    text_label = customtkinter.CTkLabel(c_app, text="This is menu item 2", font=font)
    text_label.place(relx=0.5, rely=0.5, anchor='center')


def menu_item3_click(font):
    toggle_menu()

    # Clear the window
    for widget in c_app.winfo_children():
        if widget == hamburger_button or widget == menu_frame:
            pass
        else:
            widget.destroy()

    # Display the text
    text_label = customtkinter.CTkLabel(c_app, text="This is menu item 3", font=font)
    text_label.place(relx=0.5, rely=0.5, anchor='center')


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

c_app = customtkinter.CTk()
c_app.title('Calculator')
c_app.geometry('700x700')
c_app.resizable(width=False, height=False)

font1 = ('Verdana', 30, 'bold')

# Create hamburger button
hamburger_button = customtkinter.CTkButton(c_app, command=toggle_menu, font=font1, cursor='hand2',
                                           text_color='white',
                                           hover_color='#7F8081', fg_color='#242424', text='☰', width=20)
hamburger_button.place(relx=0.03, rely=0.0919, anchor=SW)

# Create menu frame
menu_frame = customtkinter.CTkFrame(c_app, fg_color='#505253', border_color='#3A3B3C',
                                    border_width=5)

menu_item1 = customtkinter.CTkButton(menu_frame, text="Basic\nCalculator", font=('Verdana', 22, 'bold', 'italic'),
                                     width=134, height=58,
                                     text_color='white',
                                     fg_color='#505253',
                                     hover_color='#4A4A4A', anchor='w', command=lambda: menu_item1_click(font1))
menu_item1.place(relx=0.17, rely=0.033)

menu_item2 = customtkinter.CTkButton(menu_frame, text="Linear\nCo-Ordinate\nCalculator",
                                     font=('Verdana', 22, 'bold', 'italic'),
                                     width=134, height=58,
                                     text_color='white',
                                     fg_color='#505253',
                                     hover_color='#4A4A4A', anchor='w', command=lambda: menu_item2_click(font1))
menu_item2.place(relx=0.1, rely=0.14)

menu_item3 = customtkinter.CTkButton(menu_frame, text="Main Menu",
                                     font=('Verdana', 22, 'bold', 'italic'),
                                     width=134, height=26,
                                     text_color='white',
                                     fg_color='#505253',
                                     hover_color='#4A4A4A', anchor='w', command=lambda: menu_item3_click(font1))
menu_item3.place(relx=0.14, rely=0.35)

menu_item4 = customtkinter.CTkLabel(menu_frame, text=" © Jarbin Calculations",
                                    font=('Arial', 15, 'bold', 'italic'),
                                    width=100, height=26,
                                    text_color='white',
                                    fg_color='#505253',
                                    anchor='w')
menu_item4.place(relx=0.135, rely=0.95)
c_app.mainloop()
