import customtkinter
from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import pandas
from datetime import date

# lists for pandas
mode_list = []
equation_list = []
answer_list = []


def quit_application():
    plt.close()
    c_app.quit()


def save_calculations():
    # Create dataframe
    calculations_dict = {
        "Mode": mode_list,
        "Equation": equation_list,
        "Answer": answer_list
    }

    calculations_frame = pandas.DataFrame(calculations_dict)

    # create numbered index
    calculations_frame.index += 1

    # *** Get current date for heading and filename ***
    # Get today's date
    today = date.today()

    # Get day, month and year as individual strings
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    dataframe_name = f"Jarbin's Calculations ({day}_{month}_{year})"
    dataframe_heading = "*** YOUR DATA! ***"

    # change frames to strings
    calculations_txt = pandas.DataFrame.to_string(calculations_frame)

    to_write = [dataframe_name, dataframe_heading, calculations_txt]

    # create file to hold data (add .txt extension)
    file_name = f"{dataframe_name}.txt"
    text_file = open(file_name, "w+")

    # heading
    for item in to_write:
        item = f"{item}"
        text_file.write(item)
        text_file.write("\n\n")

    print()
    for item in to_write:
        print(item)
        print()

    text_file.close()

    # then quit.
    quit_application()


def finish_screen():
    for widget in c_app.winfo_children():
        widget.destroy()

    calculator_finish_menu = customtkinter.CTkFrame(c_app, fg_color='#9A9B9C', border_color='#3A3B3C',
                                                    border_width=5)
    calculator_finish_menu.place(relx=-0.02, rely=0.13, relwidth=1.03, relheight=0.75)
    calculator_finish_menu_text = customtkinter.CTkLabel(calculator_finish_menu,
                                                         text='YOU HAVE RUN OUT OF\nCALCULATIONS.',
                                                         font=('Verdana', 30, 'bold'), text_color='black')
    calculator_finish_menu_text.place(relx=0.23, rely=0.04)
    calculator_finish_menu_text_2 = customtkinter.CTkLabel(calculator_finish_menu,
                                                           text='Thank you for using Jarbin’s Calculations :)',
                                                           font=('Verdana', 24, 'italic'), text_color='black')
    calculator_finish_menu_text_2.place(relx=0.14, rely=0.19)

    calculator_quit_button = customtkinter.CTkButton(calculator_finish_menu, text='Quit',
                                                     font=('Verdana', 23, 'bold'), text_color='black',
                                                     width=80, height=40, fg_color='#9A9B9C', hover_color='#8C8D8E',
                                                     command=quit_application)
    calculator_quit_button.place(relx=0.44, rely=0.579)
    calculator_save_and_quit_button = customtkinter.CTkButton(calculator_finish_menu, text='Save and Quit',
                                                              font=('Verdana', 23, 'bold'), text_color='black',
                                                              width=140, height=40, fg_color='#9A9B9C',
                                                              hover_color='#8C8D8E', command=lambda:
                                                              save_calculations())
    calculator_save_and_quit_button.place(relx=0.365, rely=0.66)

    calculator_main_menu_button = customtkinter.CTkButton(calculator_finish_menu, text='Main Menu',
                                                          font=('Verdana', 23, 'bold'), text_color='black',
                                                          width=140, height=40, fg_color='#9A9B9C',
                                                          hover_color='#8C8D8E', command=lambda:
                                                          (main_menu(c_app, first_go=False)))
    calculator_main_menu_button.place(relx=0.395, rely=0.735)


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
                break
            else:
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


def free_roam_click():
    # Clear the window
    for widget in c_app.winfo_children():
        widget.destroy()
    run_calculators(limited_calculations=False)


def limited_calculations_click(user_amount_response):
    amount_calculations = num_checker(user_amount_response, int, 'Limited Calculations Entry',
                                      0, 50)
    if amount_calculations == '':
        messagebox.showerror('Error', 'Please enter a valid number.')
        pass
    elif amount_calculations is None:
        pass
    else:
        # Clear the window
        for widget in c_app.winfo_children():
            widget.destroy()
        run_calculators(amount_calculations)


def instructions_click():
    # Clear the window
    for widget in c_app.winfo_children():
        widget.destroy()


def run_calculators(limited_calculations=0):
    calculations_attempted = 0

    def toggle_menu():
        if menu_frame.winfo_viewable():
            menu_frame.place_forget()
        else:
            menu_frame.place(relx=-0.01, rely=-0.02, relwidth=0.302, relheight=1.03)
            for widget in c_app.winfo_children():
                if widget == hamburger_button or widget == menu_frame:
                    pass
                elif limited_calculations is not False and widget == calculations_counter:
                    pass
                else:
                    widget.destroy()

    def basic_calculator_click():
        toggle_menu()

        # Clear the window
        for widget in c_app.winfo_children():
            if widget == hamburger_button or widget == menu_frame:
                pass
            elif limited_calculations is not False and widget == calculations_counter:
                pass
            else:
                widget.destroy()

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
            global calculations_attempted
            try:
                calculations_attempted += 1

                if limited_calculations is False:
                    pass
                else:
                    calculations_counter.configure(text=f"Total Calculations:\n"
                                                        f"{calculations_attempted}/{limited_calculations}")

                equation = equation_entry.get()
                new_equation = equation.replace('x', '*')
                result = eval(new_equation)
                clear()
                equation_entry.configure(state='normal')
                equation_entry.insert(0, result)

                if calculations_attempted < (limited_calculations + 1) and limited_calculations is not False:
                    equation_list.append(equation)
                    answer_list.append(result)
                    mode_list.append("Basic")

            except (ZeroDivisionError, SyntaxError):
                messagebox.showerror('Syntax Error', 'Please enter a valid equation.')
            except TclError:
                pass

            equation_entry.configure(state='readonly')

            if calculations_attempted == (limited_calculations + 1) and limited_calculations is not False:
                finish_screen()

        font_basic = ('Verdana', 30, 'bold')

        equation_entry = customtkinter.CTkEntry(c_app, font=font_basic, width=650, height=90, state='readonly')
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
            digit_button = customtkinter.CTkButton(c_app, command=lambda t=text: button_click(t), font=font_basic,
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
            digit_button = customtkinter.CTkButton(c_app, command=lambda t=text: button_click(t), font=font_basic,
                                                   cursor='hand2', width=153, height=75,
                                                   border_color='#343638', text_color='white', text=text,
                                                   hover_color='#887148',
                                                   fg_color='#dcb575', border_width=2)
            digit_button.place(relx=relx, rely=rely)

        clear_button = customtkinter.CTkButton(c_app, command=clear, font=font_basic, cursor='hand2', width=153,
                                               height=75,
                                               border_color='#343638', text_color='white', hover_color='#7F8081',
                                               fg_color='#9A9B9C', border_width=2, text='C')
        clear_button.place(relx=0.506, rely=0.712)

        equal_button = customtkinter.CTkButton(c_app, command=calculate, font=font_basic, cursor='hand2', width=640,
                                               height=75,
                                               border_color='#343638', text_color='white', hover_color='#887148',
                                               fg_color='#dcb575', border_width=2, text='=')
        equal_button.place(relx=0.041, rely=0.849)

    def linear_calculator_click():

        toggle_menu()

        # Clear the window
        for widget in c_app.winfo_children():
            if widget == hamburger_button or widget == menu_frame or widget == calculations_counter:
                pass
            else:
                widget.destroy()

        def display_graph(graphing_values):
            try:
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

            except (UserWarning, RuntimeWarning):
                pass

        # Retrieve and format linear equation
        def linear_equation_evaluator():
            try:
                global calculations_attempted
                calculations_attempted += 1

                if limited_calculations is False:
                    pass
                else:
                    calculations_counter.configure(text=f"Total Calculations:\n "
                                                        f"{calculations_attempted}/{limited_calculations}")

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
                        string_equation = f"y = {linear_m_value} * {linear_xy_value} + {linear_c_value}"
                    else:
                        # (    y      )        = (     m     )  * (      x      ) - (      c     )
                        linear_equation_answer = linear_m_value * linear_xy_value - linear_c_value
                        string_equation = f"y = {linear_m_value} * {linear_xy_value} - {linear_c_value}"

                else:
                    if linear_equation_operator == '+':
                        # (       x          ) = (      y      )  - ((      m       ) + (      c     ))
                        linear_equation_answer = linear_xy_value - (linear_m_value + linear_c_value)
                        string_equation = f"x = {linear_xy_value} - ({linear_m_value} + {linear_c_value})"
                    else:
                        # (       x          ) = (      y      )  - ((      m       ) + (      c     ))
                        linear_equation_answer = linear_xy_value - (linear_m_value - linear_c_value)
                        string_equation = f"x = {linear_xy_value} - ({linear_m_value} - {linear_c_value})"

                linear_equation_answer_output = f'{linear_equation_answer:.2f}'.strip('.00')

                # append for pandas
                if calculations_attempted < (limited_calculations + 1) and limited_calculations is not False:
                    equation_list.append(string_equation)
                    answer_list.append(linear_equation_answer)
                    mode_list.append("Linear")

                if linear_x_or_y == 'x':
                    linear_other_x_or_y = 'y'
                else:
                    linear_other_x_or_y = 'x'

                linear_answer_label_text.configure(text=f'When {linear_x_or_y} = {linear_xy_value}, '
                                                        f'{linear_other_x_or_y} is...')
                linear_answer_label_text_2.configure(text=f'{linear_equation_answer_output}')

                # DISPLAY THE GRAPH!
                graph_y_equation_values = [linear_m_value, linear_equation_operator, linear_c_value]

                # Check if calculations limit reached
                if calculations_attempted >= (limited_calculations + 1) and limited_calculations is not False:
                    finish_screen()
                else:
                    display_graph(graph_y_equation_values)

            except (ValueError, TypeError, SyntaxError, UserWarning):
                messagebox.showerror('Syntax Error', 'Please enter a valid equation.')

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
        linear_operator_drop_down = customtkinter.CTkOptionMenu(c_app, values=linear_operators_list, width=43,
                                                                height=72,
                                                                font=font1,
                                                                text_color='white', fg_color='#505253',
                                                                dropdown_font=('Verdana', 18),
                                                                button_color='#3C3E3E', corner_radius=7,
                                                                dropdown_hover_color='#2D2F2F',
                                                                button_hover_color='#2D2F2F')
        linear_operator_drop_down.place(relx=0.431, rely=0.184)

        # entrybox for 'c' in y = mx + c
        linear_entrybox_c = customtkinter.CTkEntry(c_app, font=font1, width=248, height=72,
                                                   placeholder_text='          c')
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

        c_app.protocol("WM_DELETE_WINDOW", quit_application)

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
                                         hover_color='#4A4A4A', anchor='w', command=lambda: main_menu(c_app, False))
    menu_item3.place(relx=0.14, rely=0.35)

    menu_item4 = customtkinter.CTkLabel(menu_frame, text=" © Jarbin Calculations",
                                        font=('Arial', 15, 'bold', 'italic'),
                                        width=100, height=26,
                                        text_color='white',
                                        fg_color='#505253',
                                        anchor='w')
    menu_item4.place(relx=0.135, rely=0.95)

    if limited_calculations is False:
        pass
    else:
        calculations_counter = customtkinter.CTkLabel(c_app, text=f"Total Calculations:\n "
                                                                  f"0/{limited_calculations}",
                                                      width=205, height=56, fg_color='#505253', corner_radius=7,
                                                      font=('Verdana', 16, 'bold'))

        calculations_counter.place(relx=0.67, rely=0.024)


def main_menu(master, first_go=True):
    global calculations_attempted

    if first_go is False:
        # Clear the window
        for widget in c_app.winfo_children():
            widget.destroy()
        calculations_attempted = 0

    # create basic labels
    welcome_jarbin_big_label = customtkinter.CTkLabel(master, width=403, height=48, font=('Verdana', 34, 'bold'),
                                                      text="Jarbin's Calculations", text_color='white',
                                                      fg_color='#242424', bg_color='#242424', anchor='w')
    welcome_jarbin_big_label.place(relx=0.04, rely=0.18)

    welcome_free_roam_button = customtkinter.CTkButton(master, width=246, height=64, font=('Verdana', 24, 'bold'),
                                                       text='Free Roam',
                                                       text_color='white',
                                                       fg_color='#505253', corner_radius=7, anchor='w',
                                                       hover_color='#3C3E3E', command=lambda: free_roam_click())
    welcome_free_roam_button.place(relx=0.04, rely=0.292)

    welcome_limited_calculations_button = customtkinter.CTkButton(master, width=435, height=64,
                                                                  font=('Verdana', 24, 'bold'),
                                                                  text='Limited Calculations:',
                                                                  text_color='white',
                                                                  fg_color='#505253', corner_radius=7, anchor='w',
                                                                  hover_color='#3C3E3E',
                                                                  command=lambda: limited_calculations_click
                                                                  (welcome_limited_calulations_entrybox.get()))
    welcome_limited_calculations_button.place(relx=0.04, rely=0.403)

    welcome_limited_calulations_entrybox = customtkinter.CTkEntry(master, width=126, height=52,
                                                                  font=('Verdana', 20, 'bold'),
                                                                  text_color='white',
                                                                  corner_radius=7, bg_color='#505253')
    welcome_limited_calulations_entrybox.place(relx=0.47, rely=0.412)

    welcome_instructions_button = customtkinter.CTkButton(master, width=646, height=64,
                                                          font=('Verdana', 24, 'bold', 'italic'),
                                                          text='Instructions',
                                                          text_color='white',
                                                          fg_color='#505253', corner_radius=7, anchor='w',
                                                          hover_color='#3C3E3E')
    welcome_instructions_button.place(relx=0.04, rely=0.513)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

c_app = customtkinter.CTk()
c_app.title('Calculator')
c_app.geometry('700x700')
c_app.resizable(width=False, height=False)

# Calculation Counter
calculations_attempted = 0
amount_calculations_allowed = 0

main_menu(c_app)

c_app.mainloop()
