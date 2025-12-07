# tidbitwithgui.py
# TidBit Computer Store loan payment schedule (GUI version)

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


def compute_schedule():
    """Compute the TidBit payment schedule and display it in the text box."""
    try:
        rate = float(rate_entry.get()) / 100.0       # annual rate → decimal
        price = float(price_entry.get())
    except ValueError:
        output.delete("1.0", tk.END)
        output.insert(tk.END, "Error: Enter numeric values.\n")
        return

    # Down payment and monthly payment
    down_payment = 0.10 * price
    monthly_payment = 0.05 * price

    # Initial balance
    balance = price - down_payment

    # Monthly interest rate
    monthly_rate = rate / 12.0

    # Clear output box
    output.delete("1.0", tk.END)

    # Print header
    header = (
        "Month | Starting Bal | Interest | Principal | Payment | Ending Bal\n"
        + "-"*68 + "\n"
    )
    output.insert(tk.END, header)

    month = 1
    # Loop until balance is paid off
    while balance > 0:
        starting_balance = balance
        interest = starting_balance * monthly_rate

        # If the monthly payment is more than needed to finish the loan
        if monthly_payment > starting_balance + interest:
            payment = starting_balance + interest   # final payment
        else:
            payment = monthly_payment

        principal = payment - interest
        ending_balance = starting_balance - principal

        # Fix tiny negative rounding errors
        if ending_balance < 0:
            ending_balance = 0.0

        # Write to output
        line = f"{month:5d} | ${starting_balance:11.2f} | ${interest:8.2f} | "
        line += f"${principal:8.2f} | ${payment:7.2f} | ${ending_balance:10.2f}\n"
        output.insert(tk.END, line)

        # Prepare for next loop
        balance = ending_balance
        month += 1


# -------------------------------
# GUI Setup
# -------------------------------

window = tk.Tk()
window.title("TidBit Payment Schedule")

# Interest rate input
ttk.Label(window, text="Annual interest rate (%):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
rate_entry = ttk.Entry(window, width=15)
rate_entry.grid(row=0, column=1) 
rate_entry.insert(0, "12")  # sample default

# Purchase price input
ttk.Label(window, text="Purchase price ($):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
price_entry = ttk.Entry(window, width=15)
price_entry.grid(row=1, column=1)
price_entry.insert(0, "1000")  # sample default

# Compute button
compute_button = ttk.Button(window, text="Compute Schedule", command=compute_schedule)
compute_button.grid(row=2, column=0, columnspan=2, pady=10)

# Output text area (scrollable)
output = ScrolledText(window, width=80, height=20, font=("Courier", 10))
output.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
