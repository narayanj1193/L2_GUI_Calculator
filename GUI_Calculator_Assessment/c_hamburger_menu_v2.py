import customtkinter
from tkinter import *


def toggle_menu():
    if menu_frame.winfo_viewable():
        menu_frame.place_forget()
    else:
        menu_frame.place(relx=0.0, rely=0.0, relwidth=0.3, relheight=1.0)


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
menu_frame = Frame(c_app, bg='#505253', width=210, height=700)

menu_label = customtkinter.CTkLabel(menu_frame, text="Menu", font=font1)
menu_label.pack(pady=10)

menu_item1 = customtkinter.CTkButton(menu_frame, text="Item 1", font=font1, text_color='white', fg_color='#3C3E3E',
                                     hover_color='#4A4A4A', command=lambda: menu_item1_click(font1), state='normal')
menu_item1.pack(fill='x', pady=5)

menu_item2 = customtkinter.CTkButton(menu_frame, text="Item 2", font=font1, text_color='white', fg_color='#3C3E3E',
                                     hover_color='#4A4A4A', command=lambda: menu_item2_click(font1))
menu_item2.pack(fill='x', pady=5)

menu_item3 = customtkinter.CTkButton(menu_frame, text="Item 3", font=font1, text_color='white', fg_color='#3C3E3E',
                                     hover_color='#4A4A4A', command=lambda: menu_item3_click(font1))
menu_item3.pack(fill='x', pady=5)

c_app.mainloop()
