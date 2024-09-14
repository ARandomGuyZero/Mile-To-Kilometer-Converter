"""
Mile to Kilometer Converter

Author: Alan
Date: September 14th 2024

This script generates a window that shows a simple mile to kilometer converter.
The user can input a distance, and it will print the distance.
"""

from tkinter import *

def calculate_distance():
    try:
        miles = int(miles_input.get())
        kilometer = miles * 1.609
        kilometer_result_label.config(text=kilometer)
    except ValueError:
        kilometer_result_label.config(text=0)

# New window object from TK
window = Tk()

# Window configuration
window.config(padx=20, pady=20)

# Input for the user
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Label to display result
kilometer_result_label = Label(text=0)
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Button to execute the conversion
calculate_button = Button(text="Calculate", command=calculate_distance)
calculate_button.grid(column=1, row=2)

window.mainloop()
