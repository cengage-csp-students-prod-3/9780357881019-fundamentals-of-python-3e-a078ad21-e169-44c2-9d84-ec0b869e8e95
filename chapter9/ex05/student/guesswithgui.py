# guesswithgui.py
# GUI-based guess-the-number game where the computer guesses the number
# (LO: 9.2 - 9.7)

import tkinter as tk
from tkinter import ttk

# ------------------------------
# Game Logic
# ------------------------------

def new_game():
    """Start a new game: reset bounds and make the first guess."""
    global low, high, guess

    low = 1
    high = 100
    guess = (low + high) // 2

    message_label.config(text=f"Is the number {guess}?")

    # Enable guess feedback buttons
    btn_small.config(state="normal")
    btn_large.config(state="normal")
    btn_correct.config(state="normal")


def too_small():
    """User says the guess is too small → adjust range upward."""
    global low, high, guess

    low = guess + 1
    guess = (low + high) // 2
    message_label.config(text=f"Is the number {guess}?")


def too_large():
    """User says the guess is too large → adjust range downward."""
    global low, high, guess

    high = guess - 1
    guess = (low + high) // 2
    message_label.config(text=f"Is the number {guess}?")


def correct():
    """User says the guess is correct → end game."""
    message_label.config(text=f"I guessed it! The number is {guess}.")

    # Disable guess feedback buttons
    btn_small.config(state="disabled")
    btn_large.config(state="disabled")
    btn_correct.config(state="disabled")


# ------------------------------
# GUI Setup
# ------------------------------

window = tk.Tk()
window.title("Guessing Game")

# Guess message label
message_label = ttk.Label(window, text="Click 'New game' to begin.", font=("Arial", 14))
message_label.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Buttons
btn_small = ttk.Button(window, text="Too small", width=12, command=too_small, state="disabled")
btn_small.grid(row=1, column=0, padx=5, pady=10)

btn_large = ttk.Button(window, text="Too large", width=12, command=too_large, state="disabled")
btn_large.grid(row=1, column=1, padx=5, pady=10)

btn_correct = ttk.Button(window, text="Correct", width=12, command=correct, state="disabled")
btn_correct.grid(row=1, column=2, padx=5, pady=10)

btn_new = ttk.Button(window, text="New game", width=12, command=new_game)
btn_new.grid(row=1, column=3, padx=5, pady=10)

# Start main loop
window.mainloop()
