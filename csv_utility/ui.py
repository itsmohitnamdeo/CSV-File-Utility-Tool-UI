import tkinter as tk
from tkinter import messagebox
from .utility import CSVUtility

class CSVUtilityUI:
    def __init__(self, root, file_name):
        self.root = root
        self.file_name = file_name
        self.csv_tool = CSVUtility(file_name)

    def display_menu(self):
        menu_frame = tk.Frame(self.root)
        menu_frame.pack()

        tk.Button(menu_frame, text="Display Data", command=self.display_data).pack()
        tk.Button(menu_frame, text="Filter Data", command=self.filter_data).pack()
        tk.Button(menu_frame, text="Sort Data", command=self.sort_data).pack()
        tk.Button(menu_frame, text="Aggregate Data", command=self.aggregate_data).pack()
        tk.Button(menu_frame, text="Write Data to CSV", command=self.write_data).pack()
        tk.Button(menu_frame, text="Check Palindromes", command=self.check_palindromes).pack()

    def display_data(self):
        self.csv_tool.display_data(self.root)

    def filter_data(self):
        self.csv_tool.filter_rows(self.root)

    def sort_data(self):
        self.csv_tool.sort_rows(self.root)

    def aggregate_data(self):
        self.csv_tool.aggregate_data(self.root)

    def write_data(self):
        self.csv_tool.write_to_new_file(self.root)

    def check_palindromes(self):
        self.csv_tool.check_palindromes(self.root)
