import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def display_data(data, root):
    """Display the first few rows of the CSV based on user input."""
    
    # Ask the user how many rows they want to display
    num_rows = simpledialog.askinteger("Input", "Enter the number of rows to display:", minvalue=1, maxvalue=len(data))
    
    if num_rows is None:
        return  # If the user cancels or doesn't provide an input, do nothing
    
    # Get the requested number of rows and convert to string for display
    rows = data.head(num_rows).to_string(index=False)
    
    # Create a new top-level window to display the data
    display_window = tk.Toplevel(root)
    display_window.title("Display Data")
    
    # Create a text widget to display the rows
    text = tk.Text(display_window, height=10, width=50)
    text.pack(pady=10)
    
    # Insert the rows into the text widget
    text.insert(tk.END, rows)

    # Make the window non-editable
    text.config(state=tk.DISABLED)
