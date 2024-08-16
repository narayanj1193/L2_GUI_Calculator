import customtkinter
from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import pandas
from datetime import date

# Lists to store data for pandas
mode_list = []
equation_list = []
answer_list = []


# Main Menu Function to display fully functional main menu
def main_menu(master, first_go=True):
    global calculations_attempted

    # Reset calculations_attempted if it's not the first go
    if not first_go:
        # Clear all widgets in the window
        for widget in master.winfo_children():
            widget.destroy()
        calculations_attempted = 0

    # Create and place a welcome label
    welcome_jarbin_big_label = customtkinter.CTkLabel(
        master,
        width=403, height=48,
        font=('Verdana', 34, 'bold'),
        text="Jarbin's Calculations",
        text_color='white',
        fg_color='#242424', bg_color='#242424',
        anchor='w'
    )
    welcome_jarbin_big_label.place(relx=0.04, rely=0.18)

    # Create and place a button for Free Roam mode
    welcome_free_roam_button = customtkinter.CTkButton(
        master,
        width=246, height=64,
        font=('Verdana', 24, 'bold'),
        text='Free Roam',
        text_color='white',
        fg_color='#505253', corner_radius=7,
        anchor='w', hover_color='#3C3E3E',
        command=lambda: free_roam_click()
    )
    welcome_free_roam_button.place(relx=0.04, rely=0.292)

    # Create and place a button for Limited Calculations mode
    welcome_limited_calculations_button = customtkinter.CTkButton(
        master,
        width=435, height=64,
        font=('Verdana', 24, 'bold'),
        text='Limited Calculations:',
        text_color='white',
        fg_color='#505253', corner_radius=7,
        anchor='w', hover_color='#3C3E3E',
        command=lambda: limited_calculations_click(
            welcome_limited_calculations_entrybox.get()
        )
    )
    welcome_limited_calculations_button.place(relx=0.04, rely=0.403)

    # Create and place an entry box for Limited Calculations mode
    welcome_limited_calculations_entrybox = customtkinter.CTkEntry(
        master,
        width=126, height=52,
        font=('Verdana', 20, 'bold'),
        text_color='white',
        corner_radius=7, bg_color='#505253'
    )
    welcome_limited_calculations_entrybox.place(relx=0.47, rely=0.412)

    # Create and place a button for Instructions
    welcome_instructions_button = customtkinter.CTkButton(
        master,
        width=646, height=64,
        font=('Verdana', 24, 'bold', 'italic'),
        text='Instructions',
        text_color='white',
        fg_color='#505253', corner_radius=7,
        anchor='w', hover_color='#3C3E3E',
        command=lambda: current_instructions_page_setup()
    )
    welcome_instructions_button.place(relx=0.04, rely=0.513)


# number checker used within calculators to check for validity of user inputs
def num_checker(user_number, mode, error_label, lower_boundary=None, upper_boundary=None):
    while True:
        # If user_number is an empty string, return it
        if user_number == "":
            return user_number

        try:
            # Attempt to convert user_number to the specified mode (e.g., int or float)
            user_number = mode(user_number)

            # Check if user_number is within the specified boundaries
            if user_number <= lower_boundary or user_number >= upper_boundary:
                # Show an error message if it's out of bounds
                messagebox.showerror(f'ERROR ({error_label})',
                                     f"Please enter a number that is more than {lower_boundary} and less than "
                                     f"{upper_boundary}")
                break  # Exit the loop and end the function
            else:
                # Return the valid user_number
                return user_number

        except ValueError:
            # Handle invalid input by showing an error message
            if mode == int:
                error_message = f"Please enter an INTEGER that is more than {lower_boundary} and less than " \
                                f"{upper_boundary}"
            else:
                error_message = f"Please enter a valid number that is more than {lower_boundary} and less than " \
                                f"{upper_boundary}"
            messagebox.showerror(f'VALUE ({error_label})', error_message)
            return  # Exit the function


# Function called when free roam is clicked in main menu, initialises the program for run_calculators
def free_roam_click():
    # Clear all widgets in the current window
    for widget in c_app.winfo_children():
        widget.destroy()

    # Run calculators without any limitations (limited_calculations count)
    run_calculators(limited_calculations=False)


# Function called when limited calculations is selected in main menu, initialises the program for run_calculators
def limited_calculations_click(user_amount_response):
    # Check if the user's input is a valid integer within the range 0 to 50
    amount_calculations = num_checker(user_amount_response, int, 'Limited Calculations Entry', 0, 50)

    # If the input is an empty string, show an error message
    if amount_calculations == '':
        messagebox.showerror('Error', 'Please enter a valid number.')
        pass
    # If the input is None, do nothing (pass)
    elif amount_calculations is None:
        pass
    else:
        # Clear all widgets in the current window
        for widget in c_app.winfo_children():
            widget.destroy()

        # Run the calculators with the specified number of calculations
        run_calculators(amount_calculations)


# Function to set up the instructions page based on the current page number and action
def current_instructions_page_setup(page_action=None, first_go=True, page_number=None):
    # Set the starting page to 1 if this is the first time loading the instructions
    if first_go is True:
        current_page = 1
    else:
        current_page = page_number

    # Adjust the current page number based on the page_action parameter
    if page_action == 'back':
        current_page -= 1
    elif page_action == 'next':
        current_page += 1

    # Clear all widgets in the current window to prepare for the new instructions page
    for widget in c_app.winfo_children():
        widget.destroy()

    # Create and place a label to display the instructions text
    instructions_page_text_label = customtkinter.CTkLabel(
        c_app,
        width=646, height=437,
        text='',
        fg_color='#505253', corner_radius=7, anchor='w'
    )
    instructions_page_text_label.place(relx=0.04, rely=0.162)

    # Create and place the "Back" button for navigating to the previous instructions page
    instructions_main_menu_back_button = customtkinter.CTkButton(
        c_app,
        width=309, height=63,
        font=('Verdana', 24), text='Back',
        text_color='white',
        fg_color='#505253', corner_radius=7,
        hover_color='#3C3E3E',
        command=lambda: current_instructions_page_setup('back', False, current_page)
    )
    instructions_main_menu_back_button.place(relx=0.04, rely=0.818)

    # Create and place the "Next" button for navigating to the next instructions page
    instructions_main_menu_next_button = customtkinter.CTkButton(
        c_app,
        width=309, height=63,
        font=('Verdana', 24), text='Next',
        text_color='white',
        fg_color='#505253', corner_radius=7,
        hover_color='#3C3E3E',
        command=lambda: current_instructions_page_setup('next', False, current_page)
    )
    instructions_main_menu_next_button.place(relx=0.52, rely=0.818)

    # Display the appropriate instructions content based on the current page number
    if current_page == 0:
        main_menu(c_app, False)

    elif current_page == 1:
        instructions_text_1 = (
            "Jarbin's Calculations is a calculator\napplication designed with a graphical user\n"
            "interface using the customtkinter library. This\n guide provides detailed instructions on "
            "using\nthe program's features, including how to use the\nlinear calculator, saving calculations,\n"
            "and navigation within the app."
        )
        instructions_page_text_1 = customtkinter.CTkLabel(
            c_app,
            width=585, height=227,
            font=('Verdana', 24),
            text=instructions_text_1,
            text_color='white',
            fg_color='#505253', bg_color='#505253'
        )
        instructions_page_text_1.place(relx=0.08, rely=0.3)
        instructions_main_menu_back_button.configure(text='Main Menu')

    elif current_page == 2:
        instructions_text_3 = (
            "Linear Coordinate Calculator\nThe linear coordinate calculator can be used to solve linear\n"
            "equations and display the graphical representation. This\ncalculator is based on the standard "
            "linear equation: y = mx + c,\nwhere m is the gradient and c is the y-intercept value.\n\n"
            "How to use:\nInput M Value: Enter the gradient (m) of the equation in\nthe provided entry box.\n"
            "Operator: Select the operator ‘+’ or ‘-’ from the dropdown.\nInput C Value: Enter the y-intercept (c)"
            " in the provided\nentry box.\nX/Y Dropdown: Select whether the known variable is x or\ny. The calculator"
            "solves for the remaining unknown\nvariable.\nInput X/Y Value: Enter the value of the known variable.\n"
            "Calculate: Click the ‘CALCULATE’ button to compute the\nresult and display the graph."
        )
        instructions_page_text_3 = customtkinter.CTkLabel(
            c_app,
            width=585, height=210,
            font=('Verdana', 18),
            text=instructions_text_3,
            text_color='white',
            fg_color='#505253', bg_color='#505253'
        )
        instructions_page_text_3.place(relx=0.08, rely=0.18)
        instructions_main_menu_back_button.configure(text='Back')
        instructions_main_menu_next_button.configure(text='Next')

    elif current_page == 3:
        instructions_text_4 = (
            "Saving Calculations\nNote: To save your data you must be using the limited\ncalculations mode.\n\n"
            "How to Save\nSave and Quit: When you have reached your\nmaximum calculations in the limited calculations\n"
            "mode you will be given the prompt ‘Save and Quit’,\nsimply click this.\n\nYour data will be stored in a"
            "pandas dataframe that will\nbe printed in the terminal. This dataframe is also\nconverted to a string and"
            "written to a text file."
        )
        instructions_page_text_4 = customtkinter.CTkLabel(
            c_app,
            width=585, height=210,
            font=('Verdana', 20),
            text=instructions_text_4,
            text_color='white',
            fg_color='#505253', bg_color='#505253'
        )
        instructions_page_text_4.place(relx=0.08, rely=0.23)
        instructions_main_menu_next_button.configure(text='Finish')

    elif current_page == 4:
        main_menu(c_app, False)


# Function called to run calculator gui.
def run_calculators(limited_calculations=0):
    # Initialize the counter for attempted calculations
    calculations_attempted = 0

    # toggle hamburger menu, contains fully functioning menu
    def toggle_menu():
        # Check if the menu frame is currently visible
        if menu_frame.winfo_viewable():
            # Hide the menu frame if it is visible
            menu_frame.place_forget()
        else:
            # Show the menu frame in the specified position and size if it is not visible
            menu_frame.place(relx=-0.01, rely=-0.02, relwidth=0.302, relheight=1.03)

            # Loop through all widgets in the current window
            for widget in c_app.winfo_children():
                # Skip the hamburger button and the menu frame itself
                if widget == hamburger_button or widget == menu_frame:
                    pass
                # Skip the calculations counter if limited_calculations is not False
                elif limited_calculations is not False and widget == calculations_counter:
                    pass
                else:
                    # Destroy all other widgets
                    widget.destroy()

    # when linear calculator is clicked in hamburger menu this function is called
    def linear_calculator_click(first_go=False):

        if first_go is True:
            pass
        else:
            # Handle the linear calculator button click
            toggle_menu()

        # Clear the window, preserving the hamburger button, menu frame, and calculation counter
        for widget in c_app.winfo_children():
            if widget == hamburger_button or widget == menu_frame or widget == calculations_counter:
                pass
            else:
                widget.destroy()

        # display graph on gui using matplotlib and canvas embedding
        def display_graph(graphing_values):
            # Display the linear graph based on the given values

            try:
                graph_equation_m_value, graph_equation_operator, graph_equation_c_value = graphing_values

                # ** Initialize the graph **

                # Create figure and axis
                fig, ax = plt.subplots(figsize=(6.4, 3.13))

                # Set x and y limits for graph
                if graph_equation_m_value == 0:
                    ax.set_xlim(-20, 20)
                    ax.axhline(y=graph_equation_c_value, color='#1F77B4')
                elif graph_equation_m_value > 0:
                    ax.set_xlim((graph_equation_m_value * -5), (graph_equation_m_value * 5))
                else:
                    ax.set_xlim((graph_equation_m_value * 5), (graph_equation_m_value * -5))

                if graph_equation_c_value == 0:
                    ax.set_ylim(-20, 20)
                elif graph_equation_c_value < 0:
                    ax.set_ylim((graph_equation_c_value * 5), (graph_equation_c_value * -5))
                else:
                    ax.set_ylim((graph_equation_c_value * -5), (graph_equation_c_value * 5))

                # Set labels and title for the graph
                ax.set_xlabel('x - axis', fontsize=10, labelpad=3)
                ax.set_ylabel('y - axis', fontsize=10, labelpad=0)
                ax.set_title('Linear Graph', fontsize=9)

                # Draw horizontal axis line at y = 0
                ax.axhline(color='black')
                # Draw vertical axis line at x = 0
                ax.axvline(color='black')

                # Add grid lines to the graph
                ax.grid()

                # Adjust layout of the figure
                fig.tight_layout()
                fig.subplots_adjust(left=0.12, right=0.95, top=0.9, bottom=0.15)

                # ** Line Details **
                graph_equation_x = np.linspace((graph_equation_m_value * -5), (graph_equation_m_value * 5), 100000)

                if graph_equation_operator == '+':
                    graph_equation_y = graph_equation_m_value * graph_equation_x + graph_equation_c_value
                else:
                    graph_equation_y = (graph_equation_m_value * graph_equation_x) - graph_equation_c_value

                # Plot the linear equation on the graph
                ax.plot(graph_equation_x, graph_equation_y, linewidth=1.5)

                # Embed the plot in the Tkinter window
                canvas = FigureCanvasTkAgg(fig, master=c_app)
                canvas.draw()
                graph_widget = canvas.get_tk_widget()
                graph_widget.place(relx=0.04, rely=0.52)
                c_app.update()

            except (UserWarning, RuntimeWarning):
                pass

        # calculator for linear equation, solves for unknown variable
        def linear_equation_evaluator():
            # Evaluate and display the result of a linear equation

            try:
                global calculations_attempted

                # Retrieve and validate the input values
                linear_m_value = num_checker(linear_entrybox_m.get(), float, 'M entry box', -500, 500)
                linear_c_value = num_checker(linear_entrybox_c.get(), float, 'C entry box', -99999, 99999)
                linear_x_or_y = linear_xy_dropdown.get()
                linear_xy_value = num_checker(linear_entrybox_xy_value.get(), float, 'X/Y entry box', -99999, 99999)
                linear_equation_operator = linear_operator_drop_down.get()

                # Format and solve the equation based on the selected variable
                if linear_x_or_y == 'x':
                    if linear_equation_operator == '+':
                        # Calculate y = m * x + c
                        linear_equation_answer = linear_m_value * linear_xy_value + linear_c_value
                        string_equation = f"y = {linear_m_value} * {linear_xy_value} + {linear_c_value}"
                    else:
                        # Calculate y = m * x - c
                        linear_equation_answer = linear_m_value * linear_xy_value - linear_c_value
                        string_equation = f"y = {linear_m_value} * {linear_xy_value} - {linear_c_value}"
                else:
                    if linear_equation_operator == '+':
                        # Calculate x = y - (m + c)
                        linear_equation_answer = linear_xy_value - (linear_m_value + linear_c_value)
                        string_equation = f"x = {linear_xy_value} - ({linear_m_value} + {linear_c_value})"
                    else:
                        # Calculate x = y - (m - c)
                        linear_equation_answer = linear_xy_value - (linear_m_value - linear_c_value)
                        string_equation = f"x = {linear_xy_value} - ({linear_m_value} - {linear_c_value})"

                # Format the answer for display
                linear_equation_answer_output = f'{linear_equation_answer:.2f}'

                calculations_attempted += 1

                # Update the calculations counter if there is a limit
                if limited_calculations is not False:
                    calculations_counter.configure(
                        text=f"Total Calculations:\n{calculations_attempted}/{limited_calculations}")

                # Append data for pandas if within the calculation limit
                if calculations_attempted < (limited_calculations + 1) and limited_calculations is not False:
                    equation_list.append(string_equation)
                    answer_list.append(linear_equation_answer)
                    mode_list.append("Linear")

                # Determine the other variable
                if linear_x_or_y == 'x':
                    linear_other_x_or_y = 'y'
                else:
                    linear_other_x_or_y = 'x'

                # Update the labels to display the answer
                linear_answer_label_text.configure(
                    text=f'When {linear_x_or_y} = {linear_xy_value}, {linear_other_x_or_y} is...')
                linear_answer_label_text_2.configure(text=f'{linear_equation_answer_output}')

                # Display the graph
                graph_y_equation_values = [linear_m_value, linear_equation_operator, linear_c_value]

                # Check if the calculation limit has been reached
                if calculations_attempted >= (limited_calculations + 1) and limited_calculations is not False:
                    finish_screen()
                else:
                    display_graph(graph_y_equation_values)

            except (ValueError, TypeError, SyntaxError, UserWarning):
                # Handle errors and show an error message
                messagebox.showerror('Syntax Error', 'Please enter a valid equation.')

        # Create a list of basic labels with their text and positions
        linear_basic_labels_list = [
            ('y', 0.04, 0.184), ('=', 0.115, 0.184), ('x', 0.359, 0.184),
            ('=', 0.204, 0.3)
        ]

        # Create and place basic labels using a loop
        for text, relx, rely in linear_basic_labels_list:
            linear_basic_labels = customtkinter.CTkLabel(
                c_app, width=43, height=72, font=font1, text=text,
                text_color='white', fg_color='#505253', corner_radius=7)
            linear_basic_labels.place(relx=relx, rely=rely)
            linear_basic_labels.lower()  # Lower the label to the back of the stacking order

        # Create and place the entry box for 'm' in the equation y = mx + c
        linear_entrybox_m = customtkinter.CTkEntry(
            c_app, font=font1, width=108, height=72, placeholder_text='   m')
        linear_entrybox_m.place(relx=0.19, rely=0.184)

        # Create and place the dropdown menu for operators (+ or -)
        linear_operators_list = ['+', '-']
        linear_operator_drop_down = customtkinter.CTkOptionMenu(
            c_app, values=linear_operators_list, width=43, height=72, font=font1,
            text_color='white', fg_color='#505253', dropdown_font=('Verdana', 18),
            button_color='#3C3E3E', corner_radius=7, dropdown_hover_color='#2D2F2F',
            button_hover_color='#2D2F2F')
        linear_operator_drop_down.place(relx=0.431, rely=0.184)

        # Create and place the entry box for 'c' in the equation y = mx + c
        linear_entrybox_c = customtkinter.CTkEntry(
            c_app, font=font1, width=248, height=72, placeholder_text='          c')
        linear_entrybox_c.place(relx=0.605, rely=0.184)

        # Create and place the dropdown menu for selecting whether the known value is x or y
        linear_xy_dropdown = customtkinter.CTkOptionMenu(
            c_app, values=['x', 'y'], width=43, height=72, font=font1,
            text_color='white', fg_color='#505253', dropdown_font=('Verdana', 18),
            button_color='#3C3E3E', corner_radius=7, dropdown_hover_color='#2D2F2F',
            button_hover_color='#2D2F2F')
        linear_xy_dropdown.place(relx=0.04, rely=0.3)

        # Create and place the entry box for the user to enter the known x or y value
        linear_entrybox_xy_value = customtkinter.CTkEntry(
            c_app, font=font1, width=135, height=72)
        linear_entrybox_xy_value.place(relx=0.282, rely=0.3)

        # Create and place the calculate button, which runs linear_equation_evaluator when clicked
        linear_button_calculate = customtkinter.CTkButton(
            c_app, width=642, height=48, font=('Verdana', 18, 'italic', 'bold'),
            border_color='#343638', text_color='white', text='CALCULATE',
            hover_color='#3C3E3E', fg_color='#505253', border_width=2,
            command=linear_equation_evaluator)
        linear_button_calculate.place(relx=0.04, rely=0.42)

        # Create and place the answer box for displaying outputs
        linear_answer_label_box = customtkinter.CTkLabel(
            c_app, width=328, height=72, text='', fg_color='#505253', corner_radius=7)
        linear_answer_label_box.place(relx=0.49, rely=0.3)

        # Create and place the first text label for the answer output
        linear_answer_label_text = customtkinter.CTkLabel(
            c_app, width=315, height=30, fg_color='#505253', bg_color='#505253',
            text_color='white', font=('Verdana', 18, 'bold', 'italic'), text='')
        linear_answer_label_text.place(relx=0.5, rely=0.3)

        # Create and place the second text label for the answer output
        linear_answer_label_text_2 = customtkinter.CTkLabel(
            c_app, width=315, height=40, fg_color='#505253', bg_color='#505253',
            text_color='white', font=('Verdana', 18, 'bold', 'italic'), text='')
        linear_answer_label_text_2.place(relx=0.5, rely=0.34)

        # Set the protocol for the window close button to quit the application
        c_app.protocol("WM_DELETE_WINDOW", quit_application)

    # Define font style for buttons and labels
    font1 = ('Verdana', 30, 'bold')

    # Create hamburger button for toggling the menu
    hamburger_button = customtkinter.CTkButton(
        c_app, command=toggle_menu, font=font1, cursor='hand2',
        text_color='white', hover_color='#7F8081', fg_color='#242424',
        text='☰', width=20)
    hamburger_button.place(relx=0.03, rely=0.0919, anchor=SW)

    # Create frame for the side menu
    menu_frame = customtkinter.CTkFrame(
        c_app, fg_color='#505253', border_color='#3A3B3C', border_width=5)

    # Create button for "Linear Co-Ordinate Calculator" in the menu
    menu_item1 = customtkinter.CTkButton(
        menu_frame, text="Linear\nCo-Ordinate\nCalculator", font=('Verdana', 22, 'bold', 'italic'),
        width=134, height=58, text_color='white', fg_color='#505253',
        hover_color='#4A4A4A', anchor='w', command=lambda: linear_calculator_click())
    menu_item1.place(relx=0.1, rely=0.05)

    # Create button for "Main Menu" in the menu
    menu_item2 = customtkinter.CTkButton(
        menu_frame, text="Main Menu", font=('Verdana', 22, 'bold', 'italic'),
        width=134, height=26, text_color='white', fg_color='#505253',
        hover_color='#4A4A4A', anchor='w', command=lambda: main_menu(c_app, False))
    menu_item2.place(relx=0.14, rely=0.35)

    # Create label for copyright information in the menu
    menu_item3 = customtkinter.CTkLabel(
        menu_frame, text=" © Jarbin Calculations", font=('Arial', 15, 'bold', 'italic'),
        width=100, height=26, text_color='white', fg_color='#505253', anchor='w')
    menu_item3.place(relx=0.135, rely=0.95)

    # Create a calculations counter if the limited_calculations is not False
    if limited_calculations is not False:
        calculations_counter = customtkinter.CTkLabel(
            c_app, text=f"Total Calculations:\n 0/{limited_calculations}",
            width=205, height=56, fg_color='#505253', corner_radius=7,
            font=('Verdana', 16, 'bold'))
        calculations_counter.place(relx=0.67, rely=0.024)

    linear_calculator_click(True)


# Function to set up the finish screen at the end of program in limited calculations
def finish_screen():
    # Destroy all widgets in the main application window
    for widget in c_app.winfo_children():
        widget.destroy()

    # Create a frame for the finish screen, and place
    calculator_finish_menu = customtkinter.CTkFrame(
        c_app, fg_color='#9A9B9C', border_color='#3A3B3C', border_width=5)
    calculator_finish_menu.place(relx=-0.02, rely=0.13, relwidth=1.03, relheight=0.75)

    # Create a label to inform the user they have run out of calculations, and place
    calculator_finish_menu_text = customtkinter.CTkLabel(
        calculator_finish_menu, text='YOU HAVE RUN OUT OF\nCALCULATIONS.',
        font=('Verdana', 30, 'bold'), text_color='black')
    calculator_finish_menu_text.place(relx=0.23, rely=0.04)

    # Create and place a thankyou label
    calculator_finish_menu_text_2 = customtkinter.CTkLabel(
        calculator_finish_menu, text="Thank you for using Jarbin’s Calculations :)",
        font=('Verdana', 24, 'italic'), text_color='black')
    calculator_finish_menu_text_2.place(relx=0.14, rely=0.19)

    # Create a quit button and palce
    calculator_quit_button = customtkinter.CTkButton(
        calculator_finish_menu, text='Quit', font=('Verdana', 23, 'bold'), text_color='black',
        width=80, height=40, fg_color='#9A9B9C', hover_color='#8C8D8E',
        command=quit_application)
    calculator_quit_button.place(relx=0.44, rely=0.579)

    # Create a "Save and Quit" button and place
    calculator_save_and_quit_button = customtkinter.CTkButton(
        calculator_finish_menu, text='Save and Quit', font=('Verdana', 23, 'bold'), text_color='black',
        width=140, height=40, fg_color='#9A9B9C', hover_color='#8C8D8E',
        command=lambda: save_calculations())
    calculator_save_and_quit_button.place(relx=0.365, rely=0.66)

    # Create a "Main Menu" button and place
    calculator_main_menu_button = customtkinter.CTkButton(
        calculator_finish_menu, text='Main Menu', font=('Verdana', 23, 'bold'), text_color='black',
        width=140, height=40, fg_color='#9A9B9C', hover_color='#8C8D8E',
        command=lambda: main_menu(c_app, first_go=False))
    calculator_main_menu_button.place(relx=0.395, rely=0.735)


# Function retrieves lists to be used in save file and converted with pandas
def save_calculations():
    # Create a dictionary to store the calculation data
    calculations_dict = {
        "Mode": mode_list,
        "Equation": equation_list,
        "Answer": answer_list
    }

    # Convert the dictionary to a pandas DataFrame
    calculations_frame = pandas.DataFrame(calculations_dict)

    # Adjust the DataFrame index to start from 1
    calculations_frame.index += 1

    # *** Get current date for heading and filename ***
    # Get today's date
    today = date.today()

    # Format the day, month, and year as strings
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    # Create the DataFrame name and heading using the current date
    dataframe_name = f"Jarbin's Calculations ({day}_{month}_{year})"
    dataframe_heading = "Calculator Stats"

    # Convert the DataFrame to a string representation
    calculations_txt = pandas.DataFrame.to_string(calculations_frame)

    # List of items to write to the text file
    to_write = [dataframe_name, dataframe_heading, calculations_txt]

    # Create a text file with the DataFrame name and add a .txt extension
    file_name = f"{dataframe_name}.txt"
    text_file = open(file_name, "w+")

    # Write each item in the list to the text file with double newlines between items
    for item in to_write:
        item = f"{item}"
        text_file.write(item)
        text_file.write("\n\n")

    # Print each item to the console for verification
    for item in to_write:
        print(item)
        print()

    # Exit the application
    quit_application()


# quits application without errors.
def quit_application():
    # Close any open matplotlib plots
    plt.close()

    # Terminate the cTkinter application
    c_app.quit()


# Set the appearance mode of customtkinter to dark theme
customtkinter.set_appearance_mode("dark")

# Set the default color theme to blue
customtkinter.set_default_color_theme("blue")

# Initialize the main application window
c_app = customtkinter.CTk()

# Set the title of the application window
c_app.title('Calculator')

# Set the dimensions of the application window
c_app.geometry('700x700')

# Make the application window non-resizable
c_app.resizable(width=False, height=False)

# Initialize the calculation counter
calculations_attempted = 0

# Initialize the allowed number of calculations
amount_calculations_allowed = 0

# Call the main menu function to set up the initial UI
main_menu(c_app)

# Run the main event loop of the application
c_app.mainloop()
