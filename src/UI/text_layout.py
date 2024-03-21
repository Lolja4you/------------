import tkinter as tk


class LogText(tk.Text):
    def __init__(self, master, height, width):
        super().__init__(master, height=height, width=width)
        self.tag_configure("green", foreground="green")
        self.tag_configure("red", foreground="red")
        self.tag_configure("yellow", foreground="yellow")
        self.tag_configure("orange", foreground="orange")
        self.tag_configure("dBlue", foreground="#000033")
        self.tag_configure("blue", foreground="#0000ff")