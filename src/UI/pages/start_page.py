import datetime

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


import mplcursors

from src.UI.base_page_class import BaseWindow 
from src.UI.pages import settings_page
from src.UI.layouts import plot_layout, text_layuot

class StartPage(BaseWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.process_running = False
        self.settings = False

        self.tool_frame = tk.Frame(self, bd=2)
        self.tool_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # 
        # 
        # Контейнер под кнопки
        self.log_formats = datetime.datetime.now().strftime(f"[%H:%M:%S %Y-%m-%d] ")
        self.button_font = ('Helvetica', 10)


        self.button_frame = tk.Frame(self.tool_frame)
        self.button_frame.pack(side=tk.TOP)

        # Buttons
        self.start_button = tk.Button(self.button_frame, text="Старт", command=self.start_action, font=self.button_font)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.button_frame, text="Стоп", command=self.stop_action, font=self.button_font)
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.button_frame, text="Сброс", command=self.reset_action, font=self.button_font)
        self.reset_button.pack(side=tk.LEFT)

        self.graphs_button = tk.Button(self.button_frame, text="Сменить вид`    ", command=self.open_split_plot, font=self.button_font)
        self.graphs_button.pack(side=tk.LEFT)

        self.settings_button = tk.Button(self.button_frame, text="Настройки", command=self.open_settings_page, font=self.button_font)
        self.settings_button.pack(side=tk.LEFT)
        
        # Лог данных
        self.log_text = text_layuot.LogText(self.tool_frame, height=int(self.y/2), width=45)
        self.log_text.pack(side=tk.BOTTOM, fill=tk.Y)


        # Line plot
        self.fig = plt.figure(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        #Data init
        self.data = self.data_storage.get_format() 
        self.plot_drawer = plot_layout.PlotHelper(self.data_storage, self.log_text, self.canvas, self.fig)

        self.start_action()
        
    def update_plot(self):
        self.plot_drawer.update_plot()
        self.fn_repeat_id1 = self.after(2000, self.update_plot)

    def start_action(self):
        if not self.process_running or not self.settings:
            # Add your start action logic here
            self.log_text.insert(tk.END, self.log_formats + "Start action triggered\n", "green")
            self.update_plot()
            self.process_running = True
        else:
            self.log_text.insert(tk.END, self.log_formats + "Достигнут максимальный поток исполнения\n", "red")

    def stop_action(self):
        if self.process_running or self.settings:
            # Add your stop action logic here
            self.log_text.insert(tk.END, self.log_formats + "Stop action triggered\n", "red")
            self.after_cancel(self.fn_repeat_id1)
            self.process_running = False
        else:
            self.log_text.insert(tk.END, self.log_formats + "Поток исполнения был прекращен ранее\n", "red")

    def reset_action(self):
        # Add your reset action logic here
        self.log_text.delete(1.0, tk.END)
        self.log_text.insert(tk.END, "Reset action triggered\n", "orange")
        self.plot_drawer.ax.clear()
        self.canvas.draw()
        
        self.data_storage.data.drop(self.data_storage.data.index, inplace=True)

    def open_settings_page(self):
        self.settings = True
        self.stop_action()
        page = settings_page.SettingsPage(self.data_storage)
        page.protocol("WM_DELETE_WINDOW", lambda: (page.destroy(), setattr(self, 'settings', False), self.start_action()))
        page.mainloop()


    def open_split_plot(self):
        self.plot_drawer.split = not self.plot_drawer.split
        self.plot_drawer.update_plot()
        # self.canvas.draw()

    def on_close(self, event=None):
        plt.close(self.fig) 
        return super().on_close(event)