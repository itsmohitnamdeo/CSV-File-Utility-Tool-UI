import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd

def check_palindromes(data, root):
    """Check for palindromes in a specified column using only the letters A, D, V, B, N."""
    
    # Ensure the dataset is not empty
    if data.empty:
        messagebox.showerror("Error", "The dataset is empty. No data to check.")
        return None
    
    # Ask the user for the column name
    column_name = simpledialog.askstring("Input", "Enter column name to check for palindromes:", parent=root)
    
    if not column_name:
        messagebox.showerror("Error", "No column name entered.")
        return None
    
    # Check if the column exists
    if column_name not in data.columns:
        messagebox.showerror("Error", f"Column '{column_name}' does not exist.")
        return None
    
    # Handle missing values
    if data[column_name].isnull().all():
        messagebox.showerror("Error", f"Column '{column_name}' contains only missing values.")
        return None
    elif data[column_name].isnull().any():
        messagebox.showwarning("Warning", f"Column '{column_name}' contains missing values. They will be ignored.")
    
    # Define valid characters for palindrome check
    valid_chars = {'A', 'D', 'V', 'B', 'N'}
    palindromes = []  # Store palindromes found
    
    try:
        # Iterate through non-null values in the column
        for value in data[column_name].dropna().astype(str):
            clean_value = value.upper().strip()  # Convert to uppercase & remove extra spaces
            
            # Check if all characters are valid
            if all(char in valid_chars for char in clean_value):
                # Check if it's a palindrome
                if clean_value == clean_value[::-1]:
                    palindromes.append(value)
        
        # Display results
        if palindromes:
            palindromes_list = '\n'.join(palindromes)
            messagebox.showinfo("Palindrome Count", f"Number of palindromes: {len(palindromes)}\nPalindromes found:\n{palindromes_list}")
        else:
            messagebox.showinfo("Palindrome Count", f"No valid palindromes found in '{column_name}'.")
    
    except Exception as e:
        messagebox.showerror("Error", f"Palindrome check failed: {e}")
    
    return palindromes
