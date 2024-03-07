import tkinter as tk
import datetime
import matplotlib.pyplot as plt


class ButtonFrame(tk.Frame):
    def __init__(self, master, start_page):
        super().__init__(master)

        self.start_page = start_page


        self.master = master

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(side=tk.TOP)

        self.start_button = tk.Button(self.button_frame, text="Старт", command=self.start_action, font=self.button_font)
        self.start_button.pack(side=tk.LEFT)
        
        self.stop_button = tk.Button(self.button_frame, text="Стоп", command=self.stop_action, font=self.button_font)
        self.stop_button.pack(side=tk.LEFT)
        
        self.reset_button = tk.Button(self.button_frame, text="Сброс", command=self.reset_action, font=self.button_font)
        self.reset_button.pack(side=tk.LEFT)
        
        self.graphs_button = tk.Button(self.button_frame, text="Разделенные графики", command=self.open_split_plot, font=self.button_font)
        self.graphs_button.pack(side=tk.LEFT)
        
        self.settings_button = tk.Button(self.button_frame, text="Настройки", command=self.reset_action, font=self.button_font)
        self.settings_button.pack(side=tk.LEFT)
        self.start_action()

    def start_action(self):
        if not self.start_page.process_running:
            # Add your start action logic here
            self.start_page.log_text.insert(tk.END, self.log_formats + "Start action triggered\n", "green")
            self.start_page.plot_drawer.update_plot()
            self.start_page.process_running = True
            self.fn_repeat_id1 = self.after(1000, self.start_page.plot_drawer.update_plot())
        else:
            self.start_page.log_text.insert(tk.END, self.log_formats + "Достигнут максимальный поток исполнения\n", "red")

    def stop_action(self):
        if self.start_page.process_running:
            # Add your stop action logic here
            self.start_page.log_text.insert(tk.END, self.log_formats + "Stop action triggered\n", "red")
            self.after_cancel(self.fn_repeat_id1)
            self.start_page.process_running = False

    def reset_action(self):
        # Add your reset action logic here
        self.start_page.log_text.delete(1.0, tk.END)
        self.start_page.log_text.insert(tk.END,  self.log_formats + "Reset action triggered\n", "orange")
        self.start_page.ax.clear()
        self.start_page.canvas.draw()
        self.start_page.data_storage.data.drop(self.data_storage.data.index, inplace=True)

    def open_split_plot(self):...

