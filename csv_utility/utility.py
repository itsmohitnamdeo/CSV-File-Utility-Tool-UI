import pandas as pd
from .display import display_data
from .filter import filter_rows
from .sort import sort_rows
from .aggregate import aggregate_data
from .write import write_to_new_file
from .palindrome import check_palindromes


class CSVUtility:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = pd.read_csv(file_name)

    def display_data(self, root):
        display_data(self.data, root)

    def filter_rows(self, root):
        self.data = filter_rows(self.data, root)

    def sort_rows(self, root):
        self.data = sort_rows(self.data, root)

    def aggregate_data(self, root):
        aggregate_data(self.data, root)

    def write_to_new_file(self, root):
        write_to_new_file(self.data, root)

    def check_palindromes(self, root):
        check_palindromes(self.data, root)
