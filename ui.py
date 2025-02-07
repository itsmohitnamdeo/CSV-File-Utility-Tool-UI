from tkinter import *
from tkinter import messagebox
from csv_utility.utility import CSVUtility
import pandas as pd

class CSVUtilityUI:
    def __init__(self, master):
        self.master = master
        self.master.title("CSV Utility")
        self.master.geometry("600x500")
        
        self.csv_tool = None  # Initialize with None
        self.current_step = 1  # Track the current step in the process
        
        # Task-specific labels and buttons will be updated dynamically
        self.label = Label(master, text="Welcome to CSV Utility", font=("Helvetica", 14))
        self.label.pack(pady=10)
        
        self.task_frame = Frame(master)
        self.task_frame.pack(pady=20)
        
        self.step_buttons_frame = Frame(master)
        self.step_buttons_frame.pack(pady=10)
        
        self.update_step()

    def update_step(self):
        """Update the UI based on the current step."""
        for widget in self.task_frame.winfo_children():
            widget.destroy()  # Clear the previous content
        
        for widget in self.step_buttons_frame.winfo_children():
            widget.destroy()  # Clear previous buttons

        if self.current_step == 1:
            self.load_csv_step()
        elif self.current_step == 2:
            self.view_data_step()
        elif self.current_step == 3:
            self.data_operations_step()
        elif self.current_step == 4:
            self.save_data_step()
    
    def load_csv_step(self):
        """Step 1: Load the CSV file."""
        self.label.config(text="Step 1: Load CSV File")
        
        self.file_entry = Entry(self.task_frame, width=40)
        self.file_entry.pack(pady=10)
        
        self.load_button = Button(self.task_frame, text="Load CSV", command=self.load_csv)
        self.load_button.pack(pady=10)

    def load_csv(self):
        """Load the CSV file."""
        file_name = self.file_entry.get()
        try:
            self.csv_tool = CSVUtility(file_name)
            self.current_step = 2  # Proceed to Step 2 if successful
            self.update_step()  # Update UI to next step
            messagebox.showinfo("Success", "CSV file loaded successfully.")
        except FileNotFoundError:
            messagebox.showerror("Error", f"The file '{file_name}' was not found!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def view_data_step(self):
        """Step 2: Display the data."""
        self.label.config(text="Step 2: View CSV Data")
        
        if self.csv_tool and self.csv_tool.data is not None:
            data = self.csv_tool.data.head().to_string()  # Display the first few rows of the CSV
        else:
            data = "No data loaded yet."

        self.data_text = Text(self.task_frame, wrap=WORD, height=10, width=50)
        self.data_text.insert(INSERT, data)
        self.data_text.pack(pady=10)
        
        self.next_button = Button(self.step_buttons_frame, text="Next: Data Operations", command=self.next_step)
        self.next_button.pack(pady=5)

    def data_operations_step(self):
        """Step 3: Perform data operations (Add, Edit, Delete)."""
        self.label.config(text="Step 3: Perform Data Operations")
        
        self.operation_label = Label(self.task_frame, text="Choose Operation: Add, Edit, or Delete Row")
        self.operation_label.pack(pady=10)
        
        self.add_button = Button(self.task_frame, text="Add Row", command=self.add_row)
        self.add_button.pack(pady=5)
        
        self.edit_button = Button(self.task_frame, text="Edit Row", command=self.edit_row)
        self.edit_button.pack(pady=5)
        
        self.delete_button = Button(self.task_frame, text="Delete Row", command=self.delete_row)
        self.delete_button.pack(pady=5)
        
        self.next_button = Button(self.step_buttons_frame, text="Next: Save Data", command=self.next_step)
        self.next_button.pack(pady=5)

    def add_row(self):
        """Add a new row to the CSV data."""
        new_data = {"Column1": "Value1", "Column2": "Value2"}  # Example row
        self.csv_tool.data = self.csv_tool.data.append(new_data, ignore_index=True)
        messagebox.showinfo("Info", "New row added successfully.")

    def edit_row(self):
        """Edit an existing row in the CSV data."""
        self.csv_tool.data.at[0, "Column1"] = "EditedValue"  # Example edit
        messagebox.showinfo("Info", "Row edited successfully.")

    def delete_row(self):
        """Delete a row from the CSV data."""
        self.csv_tool.data = self.csv_tool.data.drop(0)  # Example delete (first row)
        messagebox.showinfo("Info", "Row deleted successfully.")
    
    def save_data_step(self):
        """Step 4: Save the CSV data."""
        self.label.config(text="Step 4: Save Data")
        
        self.save_button = Button(self.task_frame, text="Save Data", command=self.save_data)
        self.save_button.pack(pady=10)
        
    def save_data(self):
        """Save the updated CSV data."""
        try:
            self.csv_tool.data.to_csv(self.file_entry.get(), index=False)
            messagebox.showinfo("Success", "CSV file saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file: {str(e)}")

    def next_step(self):
        """Go to the next step."""
        self.current_step += 1
        if self.current_step > 4:
            self.current_step = 1  # Loop back to step 1 if needed
        self.update_step()

if __name__ == "__main__":
    root = Tk()
    app = CSVUtilityUI(root)
    root.mainloop()
