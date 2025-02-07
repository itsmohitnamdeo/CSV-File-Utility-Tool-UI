import tkinter as tk
from tkinter import simpledialog, messagebox

def write_to_new_file(data, root):
    """Write the modified data to a new CSV file."""
    # Ask the user for the new file name
    output_file = simpledialog.askstring("Input", "Enter the name for the new CSV file:", parent=root)
    
    try:
        # Write the data to the new CSV file
        data.to_csv(output_file, index=False)
        
        # Show a success message
        messagebox.showinfo("Success", f"Data written to {output_file}")
    except Exception as e:
        # Show an error message if writing to the file fails
        messagebox.showerror("Error", f"Failed to write data: {e}")
