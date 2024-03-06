import tkinter as tk 


class BaseWindow(tk.Tk):
    def __init__(self, DataStorage):
        super().__init__()

        self.data_storage = DataStorage

        self.x = self.winfo_screenwidth()
        self.y = self.winfo_screenheight()
        self.title("Исследование зависимости сопротивления резисторов от температуры")
        self.minsize(int(self.x/2), int(self.y/2))  # Set the minimum size of the window
        self.resizable(True, True) 
        
        self.configure(background="#484848")

        self.state('zoomed')
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.end_fullscreen)

        self.button_font = ('Helvetica', 10)

    def toggle_fullscreen(self, event=None):
        self.overrideredirect(not self.overrideredirect())
        return "break"
    
    def end_fullscreen(self, event=None):
        self.overrideredirect(0)
        return "break"
    
    def on_close(self, event=None):
        self.destroy()

