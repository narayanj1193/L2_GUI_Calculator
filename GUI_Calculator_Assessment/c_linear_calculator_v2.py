import customtkinter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox


def customtkinter_initialise():
    # set gui(customtkinter) appearance modes
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    main = customtkinter.CTk()
    main.title('Calculator')
    main.geometry('700x700')
    main.resizable(width=False, height=False)
    return main


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


c_app = customtkinter_initialise()

# Standard Font
font1 = ('Verdana', 32, 'bold')

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
                                                        dropdown_hover_color='#2D2F2F', button_hover_color='#2D2F2F')
linear_operator_drop_down.place(relx=0.431, rely=0.184)

# entrybox for 'c' in y = mx + c
linear_entrybox_c = customtkinter.CTkEntry(c_app, font=font1, width=248, height=72, placeholder_text='          c')
linear_entrybox_c.place(relx=0.605, rely=0.184)

# dropdown menu for user to choose if they have x or y value to calculate other coordinate
linear_xy_dropdown = customtkinter.CTkOptionMenu(c_app, values=['x', 'y'], width=43, height=72, font=font1,
                                                 text_color='white', fg_color='#505253', dropdown_font=('Verdana', 18),
                                                 button_color='#3C3E3E', corner_radius=7,
                                                 dropdown_hover_color='#2D2F2F', button_hover_color='#2D2F2F')
linear_xy_dropdown.place(relx=0.04, rely=0.3)

# entrybox for user to enter the known x or y value
linear_entrybox_xy_value = customtkinter.CTkEntry(c_app, font=font1, width=135, height=72)
linear_entrybox_xy_value.place(relx=0.282, rely=0.3)

# big o'le caluclate button, runs linear_equation_evaluator when clicked.
linear_button_calculate = customtkinter.CTkButton(c_app, width=642, height=48, font=('Verdana', 18, 'italic', 'bold'),
                                                  border_color='#343638',
                                                  text_color='white', text='CALCULATE', hover_color='#3C3E3E',
                                                  fg_color='#505253', border_width=2, command=linear_equation_evaluator)
linear_button_calculate.place(relx=0.04, rely=0.42)

# Answer box for answer outputs
linear_answer_label_box = customtkinter.CTkLabel(c_app, width=328, height=72, text='',
                                                 fg_color='#505253', corner_radius=7)
linear_answer_label_box.place(relx=0.49, rely=0.3)

# answer text widgets, seperated from box for more control over positioning.
linear_answer_label_text = customtkinter.CTkLabel(c_app, width=315, height=30, fg_color='#505253', bg_color='#505253',
                                                  text_color='white', font=('Verdana', 18, 'bold', 'italic'),
                                                  text='')
linear_answer_label_text.place(relx=0.5, rely=0.3)

linear_answer_label_text_2 = customtkinter.CTkLabel(c_app, width=315, height=40, fg_color='#505253', bg_color='#505253',
                                                    text_color='white', font=('Verdana', 18, 'bold', 'italic'),
                                                    text='')
linear_answer_label_text_2.place(relx=0.5, rely=0.34)

c_app.protocol("WM_DELETE_WINDOW", quit_app_protocol)
c_app.mainloop()
