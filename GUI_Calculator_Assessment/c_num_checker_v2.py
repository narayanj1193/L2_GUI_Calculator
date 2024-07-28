from tkinter import messagebox
import customtkinter


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
def num_checker(user_number, mode, error_label, upper_boundary=None, lower_boundary=None):
    while True:

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
                error_message = f"Please enter a" '\033[1m' "valid number" '\033[0m' \
                                "that is more than {lower_boundary} and less than " \
                                f"{upper_boundary}"
            messagebox.showerror(error_message)
            return


def calculate_button():
    user_number = entry_box.get()  # Get the value from entry box
    print(user_number)
    num_checker(user_number, float, 'Entry box', 500, -500)


c_app = customtkinter_initialise()

# entrybox for user to enter the known x or y value
font1 = ('Verdana', 32, 'bold')

entry_box = customtkinter.CTkEntry(c_app, font=font1, width=300, height=72)
entry_box.place(relx=0.282, rely=0.3)

widget_calculate_button = customtkinter.CTkButton(c_app, font=font1, width=300, height=72, text='Calculate',
                                                  command=calculate_button)
widget_calculate_button.place(relx=0.282, rely=0.5)
c_app.mainloop()
