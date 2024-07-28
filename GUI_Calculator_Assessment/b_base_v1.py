import customtkinter
from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt


def toggle_menu():
    if menu_frame.winfo_viewable():
        menu_frame.place_forget()
    else:
        menu_frame.place(relx=-0.01, rely=-0.02, relwidth=0.302, relheight=1.03)
        for widget in c_app.winfo_children():
            if widget == hamburger_button or widget == menu_frame:
                pass
            else:
                # Lower all widgets so that menu can overlay
                widget.lower()


def basic_calculator_click():
    toggle_menu()

    # Clear the window
    for widget in c_app.winfo_children():
        if widget == hamburger_button or widget == menu_frame:
            pass
        else:
            widget.destroy()

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
        try:
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
        except TclError:
            pass

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

    font1 = ('Verdana', 30, 'bold')

    equation_entry = customtkinter.CTkEntry(c_app, font=font1, width=650, height=90, state='readonly')
    equation_entry.place(relx=0.5, rely=0.189, anchor=CENTER)

    # Bind key press events to the key_press function
    c_app.bind('<Key>', key_press)

    # List of button labels and their positions
    digit_buttons = [
        ('7', 0.04, 0.3), ('8', 0.272, 0.3), ('9', 0.506, 0.3),
        ('4', 0.04, 0.437), ('5', 0.272, 0.437), ('6', 0.506, 0.437),
        ('1', 0.04, 0.574), ('2', 0.272, 0.574), ('3', 0.506, 0.574),
        ('0', 0.04, 0.712), ('.', 0.272, 0.712)
    ]

    # Create buttons using a loop
    for text, relx, rely in digit_buttons:
        digit_button = customtkinter.CTkButton(c_app, command=lambda t=text: button_click(t), font=font1,
                                               cursor='hand2', width=153, height=75,
                                               border_color='#343638', text_color='white', text=text,
                                               hover_color='#3C3E3E',
                                               fg_color='#505253', border_width=2)
        digit_button.place(relx=relx, rely=rely)

    # List of button labels and their positions
    operator_buttons = [
        ('+', 0.739, 0.3),
        ('-', 0.739, 0.437),
        ('x', 0.739, 0.574),
        ('/', 0.739, 0.712)
    ]

    # Create buttons using a loop
    for text, relx, rely in operator_buttons:
        digit_button = customtkinter.CTkButton(c_app, command=lambda t=text: button_click(t), font=font1,
                                               cursor='hand2', width=153, height=75,
                                               border_color='#343638', text_color='white', text=text,
                                               hover_color='#887148',
                                               fg_color='#dcb575', border_width=2)
        digit_button.place(relx=relx, rely=rely)

    clear_button = customtkinter.CTkButton(c_app, command=clear, font=font1, cursor='hand2', width=153, height=75,
                                           border_color='#343638', text_color='white', hover_color='#7F8081',
                                           fg_color='#9A9B9C', border_width=2, text='C')
    clear_button.place(relx=0.506, rely=0.712)

    equal_button = customtkinter.CTkButton(c_app, command=calculate, font=font1, cursor='hand2', width=640, height=75,
                                           border_color='#343638', text_color='white', hover_color='#887148',
                                           fg_color='#dcb575', border_width=2, text='=')
    equal_button.place(relx=0.041, rely=0.849)


def linear_calculator_click():
    toggle_menu()

    # Clear the window
    for widget in c_app.winfo_children():
        if widget == hamburger_button or widget == menu_frame:
            pass
        else:
            widget.destroy()

    # Simple number checker to check for integers.
    def num_checker(user_number, mode, error_label, lower_boundary=None, upper_boundary=None):
        while True:
            if user_number == "":
                return user_number

            try:
                # Check that the response is an integer
                user_number = mode(user_number)

                if user_number < lower_boundary or user_number > upper_boundary:
                    messagebox.showerror(f'ERROR ({error_label})',
                                         f"Please enter a number that is more than {lower_boundary} and less than "
                                         f"{upper_boundary}")
                return user_number

            except ValueError:
                if mode == int:
                    error_message = f"Please enter an INTEGER that is more than {lower_boundary} and less than " \
                                    f"{upper_boundary}"
                else:
                    error_message = f"Please enter a valid number that is more than {lower_boundary} and less than " \
                                    f"{upper_boundary}"
                messagebox.showerror(f'VALUE  ({error_label})', error_message)
                return

    def display_graph(graphing_values):
        graph_equation_m_value, graph_equation_operator, graph_equation_c_value = graphing_values

        # ** initialise the graph **

        # Create figure and axis
        fig, ax = plt.subplots(figsize=(6.4, 3.13))

        # set x and y limits for graph
        ax.set_xlim((graph_equation_m_value * -5), (graph_equation_m_value * 5))

        if graph_equation_c_value < 0:
            ax.set_ylim((graph_equation_c_value * 5), (graph_equation_c_value * -5))
        else:
            ax.set_ylim((graph_equation_c_value * -5), (graph_equation_c_value * 5))

        # Details on graph
        ax.set_xlabel('x - axis', fontsize=10, labelpad=3)
        ax.set_ylabel('y - axis', fontsize=10, labelpad=0)
        ax.set_title('Linear Graph', fontsize=9)

        # Horizontal axis line at y = 0
        ax.axhline(color='black')
        # Vertical axis line at x = 0
        ax.axvline(color='black')

        ax.grid()

        fig.tight_layout()
        fig.subplots_adjust(left=0.12, right=0.95, top=0.9, bottom=0.15)

        # ** Line Details **
        graph_equation_x = np.linspace((graph_equation_m_value * -5), (graph_equation_m_value * 5), 100000)

        if graph_equation_operator == '+':
            graph_equation_y = graph_equation_m_value * graph_equation_x + graph_equation_c_value
        else:
            graph_equation_y = (graph_equation_m_value * graph_equation_x) - graph_equation_c_value

        # Plot graph
        ax.plot(graph_equation_x, graph_equation_y, linewidth=1.5)

        # Embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=c_app)
        canvas.draw()
        graph_widget = canvas.get_tk_widget()
        graph_widget.place(relx=0.04, rely=0.52)
        c_app.update()

    # Retrieve and format linear equation
    def linear_equation_evaluator():
        try:

            linear_m_value = num_checker(linear_entrybox_m.get(), float, 'M entry box', -500, 500)
            linear_c_value = num_checker(linear_entrybox_c.get(), float, 'C entry box', -99999, 99999)
            linear_x_or_y = linear_xy_dropdown.get()
            linear_xy_value = num_checker(linear_entrybox_xy_value.get(), float, 'X/Y entry box', -99999, 99999)

            linear_equation_operator = linear_operator_drop_down.get()

            # Format and answer the equation.
            if linear_x_or_y == 'x':
                if linear_equation_operator == '+':
                    # (    y      )        = (     m     )  * (      x      ) + (      c     )
                    linear_equation_answer = linear_m_value * linear_xy_value + linear_c_value
                else:
                    # (    y      )        = (     m     )  * (      x      ) - (      c     )
                    linear_equation_answer = linear_m_value * linear_xy_value - linear_c_value
            else:
                # (       x          ) = (      y      )  - ((      m       ) + (      c     ))
                linear_equation_answer = linear_xy_value - (linear_m_value + linear_c_value)

            linear_equation_answer_output = f'{linear_equation_answer:.2f}'.strip('.00')

            if linear_x_or_y == 'x':
                linear_other_x_or_y = 'y'
            else:
                linear_other_x_or_y = 'x'

            linear_answer_label_text.configure(text=f'When {linear_x_or_y} = {linear_xy_value}, '
                                                    f'{linear_other_x_or_y} is...')
            linear_answer_label_text_2.configure(text=f'{linear_equation_answer_output}')

            # DISPLAY THE GRAPH!
            graph_y_equation_values = [linear_m_value, linear_equation_operator, linear_c_value]

            display_graph(graph_y_equation_values)
        except (ValueError, TypeError, SyntaxError, UserWarning):
            messagebox.showerror('Syntax Error', 'Please enter a valid equation.')

    def quit_app_protocol():
        plt.close()
        c_app.quit()

    # create basic labels
    linear_basic_labels_list = [
        ('y', 0.04, 0.184), ('=', 0.115, 0.184), ('x', 0.359, 0.184),
        ('=', 0.204, 0.3)
    ]

    # create basic labels using a loop
    for text, relx, rely in linear_basic_labels_list:
        linear_basic_labels = customtkinter.CTkLabel(c_app, width=43, height=72, font=font1, text=text,
                                                     text_color='white',
                                                     fg_color='#505253', corner_radius=7)
        linear_basic_labels.place(relx=relx, rely=rely)
        linear_basic_labels.lower()

    # *** create rest of widgets - a bit trickier cannot use loop ***

    # entrybox for 'm' in y = mx + c
    linear_entrybox_m = customtkinter.CTkEntry(c_app, font=font1, width=108, height=72, placeholder_text='   m')
    linear_entrybox_m.place(relx=0.19, rely=0.184)

    # dropdown menu for operators
    linear_operators_list = ['+', '-']
    linear_operator_drop_down = customtkinter.CTkOptionMenu(c_app, values=linear_operators_list, width=43, height=72,
                                                            font=font1,
                                                            text_color='white', fg_color='#505253',
                                                            dropdown_font=('Verdana', 18),
                                                            button_color='#3C3E3E', corner_radius=7,
                                                            dropdown_hover_color='#2D2F2F',
                                                            button_hover_color='#2D2F2F')
    linear_operator_drop_down.place(relx=0.431, rely=0.184)

    # entrybox for 'c' in y = mx + c
    linear_entrybox_c = customtkinter.CTkEntry(c_app, font=font1, width=248, height=72, placeholder_text='          c')
    linear_entrybox_c.place(relx=0.605, rely=0.184)

    # dropdown menu for user to choose if they have x or y value to calculate other coordinate
    linear_xy_dropdown = customtkinter.CTkOptionMenu(c_app, values=['x', 'y'], width=43, height=72, font=font1,
                                                     text_color='white', fg_color='#505253',
                                                     dropdown_font=('Verdana', 18),
                                                     button_color='#3C3E3E', corner_radius=7,
                                                     dropdown_hover_color='#2D2F2F', button_hover_color='#2D2F2F')
    linear_xy_dropdown.place(relx=0.04, rely=0.3)

    # entrybox for user to enter the known x or y value
    linear_entrybox_xy_value = customtkinter.CTkEntry(c_app, font=font1, width=135, height=72)
    linear_entrybox_xy_value.place(relx=0.282, rely=0.3)

    # big o'le caluclate button, runs linear_equation_evaluator when clicked.
    linear_button_calculate = customtkinter.CTkButton(c_app, width=642, height=48,
                                                      font=('Verdana', 18, 'italic', 'bold'),
                                                      border_color='#343638',
                                                      text_color='white', text='CALCULATE', hover_color='#3C3E3E',
                                                      fg_color='#505253', border_width=2,
                                                      command=linear_equation_evaluator)
    linear_button_calculate.place(relx=0.04, rely=0.42)

    # Answer box for answer outputs
    linear_answer_label_box = customtkinter.CTkLabel(c_app, width=328, height=72, text='',
                                                     fg_color='#505253', corner_radius=7)
    linear_answer_label_box.place(relx=0.49, rely=0.3)

    # answer text widgets, seperated from box for more control over positioning.
    linear_answer_label_text = customtkinter.CTkLabel(c_app, width=315, height=30, fg_color='#505253',
                                                      bg_color='#505253',
                                                      text_color='white', font=('Verdana', 18, 'bold', 'italic'),
                                                      text='')
    linear_answer_label_text.place(relx=0.5, rely=0.3)

    linear_answer_label_text_2 = customtkinter.CTkLabel(c_app, width=315, height=40, fg_color='#505253',
                                                        bg_color='#505253',
                                                        text_color='white', font=('Verdana', 18, 'bold', 'italic'),
                                                        text='')
    linear_answer_label_text_2.place(relx=0.5, rely=0.34)

    c_app.protocol("WM_DELETE_WINDOW", quit_app_protocol)


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
                                     hover_color='#4A4A4A', anchor='w', command=lambda: basic_calculator_click())
menu_item1.place(relx=0.17, rely=0.033)

menu_item2 = customtkinter.CTkButton(menu_frame, text="Linear\nCo-Ordinate\nCalculator",
                                     font=('Verdana', 22, 'bold', 'italic'),
                                     width=134, height=58,
                                     text_color='white',
                                     fg_color='#505253',
                                     hover_color='#4A4A4A', anchor='w', command=lambda: linear_calculator_click())
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
