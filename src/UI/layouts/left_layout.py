import tkinter as tk


class ToolFrame(tk.Label):
    def __init__(self):
        # self.parent = parent 
        super().__init__(borderwidth=2, relief="solid", background='#484848')
