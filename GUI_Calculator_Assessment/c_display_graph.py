import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasTk
import customtkinter


# Generate graph details
def display_graph(x, y):

    fig, ax = plt.subplots(figsize=(6.5, 3.13))

    # Plot graph
    ax.plot(x, y, linewidth=1.5)

    # Set limits for the axes
    ax.set_ylim(-25, 20)
    ax.set_xlim(-20, 20)

    # Details on graph
    ax.set_xlabel('x - axis', fontsize=8, labelpad=3)
    ax.set_ylabel('y - axis', fontsize=8, labelpad=0)

    ax.set_title('Linear Graph', fontsize=9)

    # Horizontal axis line at y = 0
    ax.axhline(color='black')
    # Vertical axis line at x = 0
    ax.axvline(color='black')

    ax.grid()

    fig.tight_layout()
    fig.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.15)

    return fig



# Set appearance modes
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

c_app = customtkinter.CTk()
c_app.title('Calculator')
c_app.geometry('700x700')
c_app.resizable(width=False, height=False)

x_graph = np.linspace(-20, 20, 10000)
y_graph = 3 * x_graph + 2

fig = display_graph(x_graph, y_graph)
canvas = FigureCanvasTkAgg(fig, master=c_app)
graph_widget = canvas.get_tk_widget()
graph_widget.place(relx=0.04, rely=0.5)

canvas.draw()

graph_square = customtkinter.CTkLabel(c_app, width=642, height=300, fg_color='#505253', bg_color='#505253',
                                      text='', )

c_app.mainloop()
