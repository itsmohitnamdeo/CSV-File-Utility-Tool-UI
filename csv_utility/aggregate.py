import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd

def aggregate_data(data, root):
    """Aggregate data by performing operations like sum, average, min, and max."""
    try:
        # Check if the dataset is empty
        if data.empty:
            messagebox.showerror("Error", "The dataset is empty. No data to aggregate.")
            return None
        
        # Ask the user for the column to aggregate
        column_name = simpledialog.askstring("Input", "Enter column name to aggregate:", parent=root)
        if not column_name:
            return None
        column_name = column_name.strip()

        # Check if the column exists
        if column_name not in data.columns:
            messagebox.showerror("Error", f"Column '{column_name}' does not exist in the dataset.")
            return None

        # Check if the column contains numeric data
        if not pd.api.types.is_numeric_dtype(data[column_name]):
            messagebox.showerror("Error", f"Column '{column_name}' is not numeric. Aggregation cannot be performed.")
            return None
        
        # Handle missing values by warning the user
        if data[column_name].isnull().all():
            messagebox.showerror("Error", f"Column '{column_name}' contains only missing values. Cannot perform aggregation.")
            return None
        elif data[column_name].isnull().any():
            messagebox.showwarning("Warning", f"Column '{column_name}' contains missing values. They will be ignored in aggregation.")
        
        # Get user input for the aggregation operation
        valid_operations = {'sum': 'sum', 'average': 'mean', 'min': 'min', 'max': 'max'}
        operation = simpledialog.askstring("Input", "Enter operation (sum, average, min, max):", parent=root)
        
        if not operation:
            return None
        operation = operation.strip().lower()
        
        if operation not in valid_operations:
            messagebox.showerror("Error", "Invalid operation! Please choose from 'sum', 'average', 'min', or 'max'.")
            return None
        
        # Perform the aggregation
        result = getattr(data[column_name], valid_operations[operation])()

        # Show the result to the user
        messagebox.showinfo("Result", f"{operation.capitalize()} of '{column_name}': {result}")
        return result
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None