import datetime

import tkinter as tk


import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mplcursors

from src.UI.layouts.left_layout import ToolFrame
from src.UI.base_page_class import BaseWindow 

class StartPage(BaseWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        self.process_running = False
        self.tool_frame = tk.Frame(self, bd=2)
        self.tool_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # 
        # 
        # Контейнер под кнопки
        self.button_frame = tk.Frame(self.tool_frame)
        self.button_frame.pack(side=tk.TOP)

        # Buttons
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
        # Кнопки в отдельный файл
        # 
        # 


        # Логи даты
        # В отдельный файл 
        self.log_text = tk.Text(self.tool_frame, height=int(self.y/2), width=45)
        self.log_text.pack(side=tk.BOTTOM, fill=tk.Y)

        self.log_text.tag_configure("green", foreground="green")
        self.log_text.tag_configure("red", foreground="red")
        self.log_text.tag_configure("yellow", foreground="yellow")
        self.log_text.tag_configure("orange", foreground="orange")
        self.log_text.tag_configure("dBlue", foreground="#000033")
        self.log_text.tag_configure("blue", foreground="#0000ff")
        # В отдельный файл
    

        # Line plot
        self.colors = ['#FF0000', '#0000FF', '#006400', '#F4A460', '#00FF7F', '#FF00FF']
                  
        self.fig = plt.figure(figsize=(6, 4))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.data = self.data_storage.get_format() 
        self.start_action()

        self.canvas.mpl_connect('scroll_event', self.on_scroll)
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def update_plot(self):
        self.data = self.data_storage.get_format() 
        self.ax.clear()

        for idx, column in enumerate(self.data.columns[1:]):
            self.ax.plot(self.data['T'], self.data[column], label=column, marker='o', color=self.colors[idx % len(self.colors)])  # Используйте контрастные цвета из списка


        self.ax.grid()
        self.ax.set_xlabel('T')
        self.ax.set_ylabel('Resistance')
        self.ax.legend()
        self.ax.set_title('Data Analysis')


        last_row = self.data.iloc[-1]  # Selecting the last row of the DataFrame
    
        # Inserting column values under each header
        self.log_text.insert(tk.END, f"Start series: {last_row._name}\n", "blue")
        for col in self.data.columns:
            val = last_row[col]
            self.log_text.insert(tk.END, f"{col}: {val}\n")
        self.log_text.insert(tk.END, f"end series\n", "blue")
        
        self.log_text.see(tk.END) 

        if last_row['T'] >= 350:
            self.canvas.get_tk_widget().xview_moveto(1)

        self.canvas.draw()
        self.fn_repeat_id1 = self.after(1000, self.update_plot)
    
    def start_action(self):
        if not self.process_running:
            # Add your start action logic here
            self.log_text.insert(tk.END, datetime.datetime.now().strftime("[%H:%M:%S %Y-%m-%d] Start action triggered\n"), "green")
            self.update_plot()
            self.process_running = True
        else:
            self.log_text.insert(tk.END, datetime.datetime.now().strftime("[%H:%M:%S %Y-%m-%d] Достигнут максимальный поток исполнения\n"), "red")

    def stop_action(self):
        if self.process_running:
            # Add your stop action logic here
            self.log_text.insert(tk.END, datetime.datetime.now().strftime("[%H:%M:%S %Y-%m-%d] Stop action triggered\n"), "red")
            self.after_cancel(self.fn_repeat_id1)
            self.process_running = False

    def reset_action(self):
        # Add your reset action logic here
        self.log_text.delete(1.0, tk.END)
        self.log_text.insert(tk.END, datetime.datetime.now().strftime(f"[%H:%M:%S %Y-%m-%d] Reset action triggered\n"), "orange")
        self.ax.clear()
        self.canvas.draw()
        
        self.data_storage.data.drop(self.data_storage.data.index, inplace=True)

    def open_split_plot(self):
        from src.UI.pages.split_plot import SplitPlotPage
        page = SplitPlotPage(self.data_storage)
        plt.close(self.fig) 
        self.destroy()
        page.mainloop()




    def on_close(self, event=None):
        plt.close(self.fig) 
        return super().on_close(event)
    
        
    def on_scroll(self, event):
        xdata = event.xdata
        ydata = event.ydata

        if event.button == 'down':
            self.ax.set_xlim(xdata - (xdata - self.ax.get_xlim()[0]) * 1.1, xdata + (self.ax.get_xlim()[1] - xdata) * 1.1)
            self.ax.set_ylim(ydata - (ydata - self.ax.get_ylim()[0]) * 1.1, ydata + (self.ax.get_ylim()[1] - ydata) * 1.1)
        elif event.button == 'up':
            self.ax.set_xlim(xdata - (xdata - self.ax.get_xlim()[0]) * 0.9, xdata + (self.ax.get_xlim()[1] - xdata) * 0.9)
            self.ax.set_ylim(ydata - (ydata - self.ax.get_ylim()[0]) * 0.9, ydata + (self.ax.get_ylim()[1] - ydata) * 0.9)

        self.canvas.draw()

    def on_press(self, event):
        if event.button == 2:  # Средняя кнопка мыши
            self.x0 = event.xdata
            self.y0 = event.ydata
            self.press = True

    def on_release(self, event):
        self.press = False

    def on_motion(self, event):
        if self.press and event.button == 2:  # Средняя кнопка мыши
            dx = event.xdata - self.x0
            dy = event.ydata - self.y0
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.ax.set_xlim(xlim[0] - dx, xlim[1] - dx)
            self.ax.set_ylim(ylim[0] - dy, ylim[1] - dy)
            self.fig.canvas.draw()