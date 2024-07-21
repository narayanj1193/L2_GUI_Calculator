import customtkinter
from tkinter import *
from PIL import ImageTk, Image

def toggle_menu():
    if menu_frame.winfo_viewable():
        menu_frame.place_forget()
    else:
        menu_frame.place(relx=0.0, rely=0.0, relwidth=0.3, relheight=1.0)


def menu_item1_click():
    toggle_menu()


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

c_app = customtkinter.CTk()
c_app.title('Calculator')
c_app.geometry('700x700')
c_app.resizable(width=False, height=False)

font1 = ('Verdana', 30, 'bold')

# Create hamburger button
hamburger_img = customtkinter.CTkImage(light_image=Image.open("Hamburger_Button.png"), size=(125,125))
hamburger_button = customtkinter.CTkButton(c_app, command=toggle_menu, font=font1, cursor='hand2',
                                           text_color='white',
                                           hover_color='#7F8081', fg_color='#242424', width=20,
                                           image=hamburger_img, text='')
hamburger_button.place(relx=0.03, rely=0.0919, anchor=SW)

# Create menu frame
menu_frame = Frame(c_app, bg='#505253', width=210, height=700)

menu_label = Label(menu_frame, text="Menu", font=font1, bg='#505253', fg='white')
menu_label.pack(pady=10)

menu_item1 = Button(menu_frame, text="Item 1", font=font1, bg='#3C3E3E', fg='white', relief='flat',
                    command=menu_item1_click)
menu_item1.pack(fill='x', pady=5)

menu_item2 = Button(menu_frame, text="Item 2", font=font1, bg='#3C3E3E', fg='white', relief='flat')
menu_item2.pack(fill='x', pady=5)

menu_item3 = Button(menu_frame, text="Item 3", font=font1, bg='#3C3E3E', fg='white', relief='flat')
menu_item3.pack(fill='x', pady=5)

c_app.mainloop()
