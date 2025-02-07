import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd

def filter_rows(data, root):
    """Filter rows based on a condition."""
    
    # Check if DataFrame is empty
    if data.empty:
        messagebox.showerror("Error", "The dataset is empty. No data to filter.")
        return data
    
    # Get the column name from the user
    column_name = simpledialog.askstring("Input", "Enter column name to filter:", parent=root)
    
    # Check if column exists
    if column_name not in data.columns:
        messagebox.showerror("Error", f"Column '{column_name}' does not exist.")
        return data
    
    filtered_data = data.copy()
    
    # Handle missing values
    if filtered_data[column_name].isnull().all():
        messagebox.showerror("Error", f"Column '{column_name}' contains only missing values. No filtering possible.")
        return data
    
    while True:
        condition_type = simpledialog.askstring("Input", "Do you want to filter by numerical or string condition? (Enter 'num' or 'str'):", parent=root).strip().lower()
        
        if condition_type == 'num':
            temp_column = pd.to_numeric(filtered_data[column_name], errors='coerce')
            
            if temp_column.isnull().all():
                messagebox.showerror("Error", f"Column '{column_name}' is not numeric. Please choose a valid numeric column.")
                continue 
            
            try:
                threshold = float(simpledialog.askstring("Input", f"Enter the threshold for filtering '{column_name}':", parent=root).strip())
                operator = simpledialog.askstring("Input", "Enter the operator for comparison (>, <, >=, <=, ==, !=):", parent=root).strip()
                
                valid_operators = {'>', '<', '>=', '<=', '==', '!='}
                if operator not in valid_operators:
                    messagebox.showerror("Error", "Invalid operator. Please use one of the following: >, <, >=, <=, ==, !=.")
                    continue 
                
                # Apply the filter condition
                filtered_data = filtered_data[temp_column.astype(float).map(eval(f"lambda x: x {operator} {threshold}"))]
                break 
            
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a valid numeric threshold.")
                continue 
        
        elif condition_type == 'str':
            # Ensure column is string type
            if not pd.api.types.is_string_dtype(filtered_data[column_name]):
                messagebox.showerror("Error", f"Column '{column_name}' is not a string column. Please choose a valid string column.")
                continue 
            
            substring = simpledialog.askstring("Input", f"Enter the substring to filter '{column_name}' by:", parent=root).strip()
            filtered_data = filtered_data[filtered_data[column_name].astype(str).str.contains(substring, case=False, na=False)]
            break
        
        else:
            messagebox.showerror("Error", "Invalid input for condition type. Please enter 'num' or 'str'.")
            continue 
    
    if filtered_data.empty:
        messagebox.showinfo("Result", "No matching records found after filtering.")
    
    # Display filtered data
    filtered_window = tk.Toplevel(root)
    filtered_window.title("Filtered Data")
    text = tk.Text(filtered_window, height=10, width=50)
    text.pack()
    text.insert(tk.END, filtered_data.to_string(index=False))
    
    return filtered_data