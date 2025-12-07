# taxformwithgui.py
# Tax calculator with filing status using radio buttons
# LO: 9.7

import tkinter as tk
from tkinter import ttk

def compute_tax():
    """Compute tax based on income and filing status."""
    try:
        income = float(income_entry.get())

        # Determine tax rate based on filing status
        status = status_var.get()
        if status == "single":
            rate = 0.20
        elif status == "married":
            rate = 0.15
        elif status == "divorced":
            rate = 0.10

        tax = income * rate
        tax_label.config(text=f"Tax owed: ${tax:,.2f}")

    except ValueError:
        tax_label.config(text="Tax owed: ERROR")

# ------------------------------
# GUI Setup
# ------------------------------

window = tk.Tk()
window.title("Tax Form")

# Income label + entry
ttk.Label(window, text="Income:").grid(row=0, column=0, padx=10, pady=10)
income_entry = ttk.Entry(window, width=20)
income_entry.grid(row=0, column=1, padx=10, pady=10)
income_entry.insert(0, "0.00")   # Default value

# Filing status title
ttk.Label(window, text="Filing Status:").grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Radio Button Variable
status_var = tk.StringVar()
status_var.set("single")   # Default option

# Radio buttons
radio_single = ttk.Radiobutton(window, text="Single", variable=status_var, value="single")
radio_married = ttk.Radiobutton(window, text="Married", variable=status_var, value="married")
radio_divorced = ttk.Radiobutton(window, text="Divorced", variable=status_var, value="divorced")

radio_single.grid(row=1, column=1, sticky="w")
radio_married.grid(row=2, column=1, sticky="w")
radio_divorced.grid(row=3, column=1, sticky="w")

# Compute Button
compute_button = ttk.Button(window, text="Compute", command=compute_tax)
compute_button.grid(row=4, column=0, columnspan=2, pady=15)

# Tax output label
tax_label = ttk.Label(window, text="Tax owed: $0.00", font=("Arial", 12))
tax_label.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
