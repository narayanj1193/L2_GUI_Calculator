import customtkinter
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Set appearance modes
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

c_app = customtkinter.CTk()
c_app.title('Calculator')
c_app.geometry('700x700')
c_app.resizable(width=False, height=False)

font1 = ('Verdana', 32, 'bold')


def linear_equation_evaluator():
    try:
        m_value = float(m_equation_entry.get())
        c_value = float(c_equation_entry.get())
        x_or_y = x_y_dropdown_menu.get()
        x_y_valu = float(y_x_value.get())

        operator = operator_drop_down.get()
        if operator == "+":
            operator = '+'
        else:
            operator = '-'

        if x_or_y == 'x':
            equation = f"{m_value}*{x_y_valu} {operator} {c_value}"
        else:
            equation = f"{x_y_valu} - ({m_value} {operator} {c_value})"

        answer = sp.sympify(equation)
        answer = f'{answer:.2f}'.strip('.00')

        if x_or_y == 'x':
            other_x_y = 'y'
        else:
            other_x_y = 'x'

        answer_text.configure(text=f'When {x_or_y} = {x_y_valu} , {other_x_y} is…')
        answer_text_2.configure(text=f'{answer}')

        # Display the graph
        display_graph(m_value, c_value)

    except (ValueError, SyntaxError, sp.SympifyError):
        answer_text.configure(text='Error')
        answer_text_2.configure(text='')


def display_graph(m_value, c_value):
    x = np.linspace(-20, 20, 10000)
    y = m_value * x + c_value

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(6.4, 3.13))

    # Plot graph
    ax.plot(x, y, linewidth=1.5)

    # Set limits for the axes
    ax.set_ylim(-25, 20)
    ax.set_xlim(-20, 20)

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
    fig.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)

    # Embed the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=c_app)
    canvas.draw()
    graph_widget = canvas.get_tk_widget()
    graph_widget.place(relx=0.04, rely=0.52)


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
                                           fg_color='#505253', border_width=2, command=linear_equation_evaluator)
calculate_button.place(relx=0.04, rely=0.42)

answer_box = customtkinter.CTkLabel(c_app, width=326, height=72, text='',
                                    fg_color='#505253', corner_radius=7)
answer_box.place(relx=0.49, rely=0.3)

answer_text = customtkinter.CTkLabel(c_app, width=315, height=30, fg_color='#505253', bg_color='#505253',
                                     text_color='white', font=('Verdana', 18, 'bold', 'italic'),
                                     text='')
answer_text.place(relx=0.5, rely=0.3)
answer_text_2 = customtkinter.CTkLabel(c_app, width=315, height=40, fg_color='#505253', bg_color='#505253',
                                       text_color='white', font=('Verdana', 18, 'bold', 'italic'),
                                       text='')
answer_text_2.place(relx=0.5, rely=0.34)
answer_text.tkraise(answer_text_2)


c_app.mainloop()
