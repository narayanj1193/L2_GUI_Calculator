import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter


def display_graph(graphing_values):
    graph_equation_m_value, graph_equation_operator, graph_equation_c_value = graphing_values

    # ** initialise the graph **

    # set x and y limits for graph
    plt.xlim((graph_equation_m_value * -5), (graph_equation_m_value * 5))

    if graph_equation_c_value < 0:
        plt.ylim((graph_equation_c_value * 5), (graph_equation_c_value * -5))
    else:
        plt.ylim((graph_equation_c_value * -5), (graph_equation_c_value * 5))

    # Details on graph
    plt.xlabel('x - axis', fontsize=10, labelpad=3)
    plt.ylabel('y - axis', fontsize=10, labelpad=0)
    plt.title('Linear Graph', fontsize=9)

    # Horizontal axis line at y = 0
    plt.axhline(color='black')
    # Vertical axis line at x = 0
    plt.axvline(color='black')

    plt.grid()

    plt.tight_layout()
    plt.subplots_adjust(left=0.12, right=0.95, top=0.9, bottom=0.15)

    # ** Line Details **
    graph_equation_x = np.linspace((graph_equation_m_value * -5), (graph_equation_m_value * 5), 100000)

    if graph_equation_operator == '+':
        graph_equation_y = graph_equation_m_value * graph_equation_x + graph_equation_c_value
    else:
        graph_equation_y = (graph_equation_m_value * graph_equation_x) - graph_equation_c_value

    # Plot graph
    plt.plot(graph_equation_x, graph_equation_y, linewidth=1.5)

    # Embed the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(plt, master=c_app)
    canvas.draw()
    graph_widget = canvas.get_tk_widget()
    graph_widget.place(relx=0.04, rely=0.52)


# Set appearance modes
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

c_app = customtkinter.CTk()
c_app.title('Calculator')
c_app.geometry('700x700')
c_app.resizable(width=False, height=False)

x_graph = np.linspace(-20, 20, 10000)
y_graph = 3 * x_graph + 2


graph_square = customtkinter.CTkLabel(c_app, width=642, height=300, fg_color='#505253', bg_color='#505253',
                                      text='', )

c_app.mainloop()
