# texteditor.py
# Simple GUI text editor with open, save, and new file operations
# LO: 9.2, 9.3, 9.4, 9.6, 9.7

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText


# ------------------------------
# Button Functions
# ------------------------------

def new_file():
    """Clear the filename entry and text area."""
    filename_entry.delete(0, tk.END)
    text_area.delete("1.0", tk.END)


def open_file():
    """Open a text file and load the contents into the text widget."""
    filepath = filedialog.askopenfilename(
        title="Open File",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if filepath:
        filename_entry.delete(0, tk.END)
        filename_entry.insert(0, filepath)

        try:
            with open(filepath, "r") as f:
                contents = f.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, contents)
        except Exception as e:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, f"Error opening file:\n{e}")


def save_file():
    """Save the text widget's content into the filename specified."""
    filepath = filename_entry.get()

    # If no filename typed, ask user for a save dialog
    if not filepath:
        filepath = filedialog.asksaveasfilename(
            title="Save File",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if not filepath:
            return  # user cancelled save

        filename_entry.insert(0, filepath)

    try:
        with open(filepath, "w") as f:
            f.write(text_area.get("1.0", tk.END))
    except Exception as e:
        text_area.insert(tk.END, f"\nError saving file:\n{e}")


# ------------------------------
# GUI Window Setup
# ------------------------------

window = tk.Tk()
window.title("Simple Text Editor")


# Filename Label + Entry
ttk.Label(window, text="Filename:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

filename_entry = ttk.Entry(window, width=50)
filename_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")


# Buttons
open_button = ttk.Button(window, text="Open", width=12, command=open_file)
open_button.grid(row=0, column=2, padx=5)

save_button = ttk.Button(window, text="Save", width=12, command=save_file)
save_button.grid(row=0, column=3, padx=5)

new_button = ttk.Button(window, text="New", width=12, command=new_file)
new_button.grid(row=0, column=4, padx=5)


# Text Area with Scrollbar
text_area = ScrolledText(window, width=90, height=30, wrap="word")
text_area.grid(row=1, column=0, columnspan=5, padx=10, pady=10)


# Start the GUI event loop
window.mainloop()
