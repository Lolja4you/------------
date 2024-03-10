import tkinter as tk
import matplotlib.pyplot as plt

from src.UI.base_page_class import BaseWindow 


class SettingsPage(BaseWindow):
    def __init__(self, DataStorage):
        super().__init__(DataStorage)

        self.data_storage = DataStorage
        
        self.settings = tk.Frame(self, bd=2)
        self.settings.grid(column=0, columnspan=3, row=0)

        self.header = tk.Label(self.settings, text="Header", font=("Arial", 14))
        self.header.grid(column=0, columnspan=3, row=0)