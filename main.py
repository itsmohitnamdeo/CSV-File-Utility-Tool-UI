import tkinter as tk
from tkinter import filedialog, messagebox
from csv_utility.ui import CSVUtilityUI

def main():
    root = tk.Tk()
    root.title("CSV Utility")
    
    # Ask the user to select a CSV file from the file explorer
    file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])
    
    # Check if the user selected a file or canceled the file dialog
    if not file_path:
        messagebox.showwarning("No file selected", "You must select a CSV file to proceed.")
        return
    
    try:
        # Initialize CSVUtilityUI with the selected file
        csv_ui = CSVUtilityUI(root, file_path)
        csv_ui.display_menu()
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

if __name__ == "__main__":
    main()
