# imagebrowser.py
# Simple GIF image browser using Tkinter
# LO: 9.2, 9.3, 9.4, 9.6, 9.7

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def open_image():
    """Open a GIF image file, load it into a PhotoImage, and display it."""
    global img  # must keep a reference to avoid garbage-collection

    # Open file dialog filtered to GIF files only
    filepath = filedialog.askopenfilename(
        title="Open GIF Image",
        filetypes=[("GIF Images", "*.gif")],
        defaultextension=".gif"
    )

    if not filepath:
        return  # user cancelled

    # Update the label
    filename_var.set(filepath)

    try:
        # Load image
        img = tk.PhotoImage(file=filepath)

        # Resize canvas to fit image
        canvas.config(width=img.width(), height=img.height())

        # Display image on canvas
        canvas.create_image(0, 0, anchor="nw", image=img)

    except Exception as e:
        filename_var.set(f"Error opening image: {e}")


# ------------------------------
# GUI Setup
# ------------------------------

window = tk.Tk()
window.title("GIF Image Browser")

# Filename display
filename_var = tk.StringVar()
filename_var.set("No file selected.")

filename_label = ttk.Label(window, textvariable=filename_var)
filename_label.grid(row=0, column=0, padx=10, pady=10)

# Open button
open_button = ttk.Button(window, text="Open Image", command=open_image)
open_button.grid(row=0, column=1, padx=10, pady=10)

# Canvas where image will be displayed
canvas = tk.Canvas(window, width=400, height=300, bg="lightgray")
canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
