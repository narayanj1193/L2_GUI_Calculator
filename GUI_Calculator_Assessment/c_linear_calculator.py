import customtkinter

# Set appearance modes
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

c_app = customtkinter.CTk()
c_app.title('Calculator')
c_app.geometry('700x700')
c_app.resizable(width=False, height=False)

font1 = ('Verdana', 32, 'bold')

y_equation_widget_1 = customtkinter.CTkLabel(c_app, width=43, height=72, font=font1, text='y',
                                             text_color='white',
                                             fg_color='#505253', corner_radius=7)
y_equation_widget_1.place(relx=0.04, rely=0.184)

equal_equation_widget = customtkinter.CTkLabel(c_app, width=43, height=72, font=font1, text='=',
                                               text_color='white',
                                               fg_color='#505253', corner_radius=7)
equal_equation_widget.place(relx=0.115, rely=0.184)

m_equation_entry = customtkinter.CTkEntry(c_app, font=font1, width=198, height=72, placeholder_text='       m')
m_equation_entry.place(relx=0.19, rely=0.184)

x_equation_entry = customtkinter.CTkLabel(c_app, width=43, height=72, font=font1, text='x',
                                          text_color='white',
                                          fg_color='#505253', corner_radius=7)
x_equation_entry.place(relx=0.486, rely=0.184)

operators = ['+', '—']
operator_drop_down = customtkinter.CTkOptionMenu(c_app, values=operators, width=43, height=72, font=font1,
                                                 text_color='white', fg_color='#505253', dropdown_font=('Verdana', 18),
                                                 button_color='#3C3E3E', corner_radius=7,
                                                 dropdown_hover_color='#2D2F2F', button_hover_color='#2D2F2F')
operator_drop_down.place(relx=0.56, rely=0.184)

c_equation_entry = customtkinter.CTkEntry(c_app, font=font1, width=160, height=72, placeholder_text='      c')
c_equation_entry.place(relx=0.736, rely=0.184)

x_y_dropdown_menu = customtkinter.CTkOptionMenu(c_app, values=['x', 'y'], width=43, height=72, font=font1,
                                                text_color='white', fg_color='#505253', dropdown_font=('Verdana', 18),
                                                button_color='#3C3E3E', corner_radius=7,
                                                dropdown_hover_color='#2D2F2F', button_hover_color='#2D2F2F')
x_y_dropdown_menu.place(relx=0.04, rely=0.3)

equal_equation_widget_2 = customtkinter.CTkLabel(c_app, width=43, height=72, font=font1, text='=',
                                                 text_color='white',
                                                 fg_color='#505253', corner_radius=7)
equal_equation_widget_2.place(relx=0.204, rely=0.3)

y_x_value = customtkinter.CTkEntry(c_app, font=font1, width=135, height=72)
y_x_value.place(relx=0.282, rely=0.3)

calculate_button = customtkinter.CTkButton(c_app, width=642, height=48, font=('Verdana', 18, 'italic', 'bold'),
                                           border_color='#343638',
                                           text_color='white', text='CALCULATE', hover_color='#3C3E3E',
                                           fg_color='#505253', border_width=2)
calculate_button.place(relx=0.04, rely=0.42)

x_or_y = x_y_dropdown_menu.get()
x_y_value = y_x_value.get()
#answer_label = customtkinter.CTkLabel(c_app, width=326, height=72, font=('Verdana', 18, 'italic', 'bold'),
                                      # text=
                                      # f'''When {x_or_y} = {x_y_value}, {} is...
                                      # {}''',
                                      # text_color='white',
                                      # fg_color='#505253', corner_radius=7)
c_app.mainloop()
