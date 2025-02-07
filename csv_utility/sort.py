import tkinter as tk
from tkinter import simpledialog, messagebox

def sort_rows(data, root):
    """Sort rows by a specific column, handling both numeric and string sorting."""
    
    # Get the column name from the user
    column_name = simpledialog.askstring("Input", "Enter column name to sort by:", parent=root)
    
    # Check if column exists
    if column_name not in data.columns:
        messagebox.showerror("Error", f"Column '{column_name}' does not exist.")
        return None
    
    # Handle missing values in the column
    if data[column_name].isnull().all():
        messagebox.showerror("Error", f"Column '{column_name}' contains only missing values. Sorting is not possible.")
        return None

    # Ask the user for sorting order
    sort_order = simpledialog.askstring("Sort Order", "Enter sorting order (asc/desc):", parent=root)
    
    if sort_order not in ['asc', 'desc']:
        messagebox.showerror("Error", "Invalid input. Please enter 'asc' for ascending or 'desc' for descending.")
        return None
    
    ascending = (sort_order == 'asc')

    try:
        # Sort the data
        sorted_data = data.sort_values(by=column_name, ascending=ascending, na_position='last')

        # Display the sorted data
        sorted_window = tk.Toplevel(root)
        sorted_window.title("Sorted Data")
        text = tk.Text(sorted_window, height=10, width=50)
        text.pack()
        text.insert(tk.END, sorted_data.to_string(index=False))

    except TypeError:
        messagebox.showerror("Error", f"Column '{column_name}' contains mixed data types and cannot be sorted reliably.")

    except Exception as e:
        messagebox.showerror("Error", f"Sorting failed: {e}")

    return sorted_data
