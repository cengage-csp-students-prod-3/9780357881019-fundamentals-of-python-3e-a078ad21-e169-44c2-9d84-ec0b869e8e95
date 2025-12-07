# temperatureconverter.py
# GUI Temperature Converter: Fahrenheit <--> Celsius
# (LO: 9.2, 9.3, 9.4, 9.5, 9.6)

import tkinter as tk
from tkinter import ttk

def fahrenheit_to_celsius():
    """Converts the value in the Fahrenheit entry to Celsius."""
    try:
        f = float(fah_entry.get())
        c = (f - 32) * 5.0 / 9.0
        cel_entry.delete(0, tk.END)
        cel_entry.insert(0, f"{c:.1f}")
    except ValueError:
        cel_entry.delete(0, tk.END)
        cel_entry.insert(0, "Error")

def celsius_to_fahrenheit():
    """Converts the value in the Celsius entry to Fahrenheit."""
    try:
        c = float(cel_entry.get())
        f = (c * 9.0 / 5.0) + 32
        fah_entry.delete(0, tk.END)
        fah_entry.insert(0, f"{f:.1f}")
    except ValueError:
        fah_entry.delete(0, tk.END)
        fah_entry.insert(0, "Error")

# ----- Main Window -----
window = tk.Tk()
window.title("Temperature Converter")

# ----- Labels -----
ttk.Label(window, text="Celsius").grid(row=0, column=0, padx=10, pady=10)
ttk.Label(window, text="Fahrenheit").grid(row=0, column=1, padx=10, pady=10)

# ----- Entry Fields -----
cel_entry = ttk.Entry(window, width=15)
fah_entry = ttk.Entry(window, width=15)

cel_entry.grid(row=1, column=0, padx=10)
fah_entry.grid(row=1, column=1, padx=10)

# Startup values
cel_entry.insert(0, "0.0")
fah_entry.insert(0, "32.0")

# ----- Buttons -----
btn_f_to_c = ttk.Button(window, text=">>>>", command=fahrenheit_to_celsius)
btn_c_to_f = ttk.Button(window, text="<<<<", command=celsius_to_fahrenheit)

btn_f_to_c.grid(row=2, column=0, pady=15)
btn_c_to_f.grid(row=2, column=1, pady=15)

window.mainloop()
