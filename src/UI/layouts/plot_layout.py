# plot_helper.py

import tkinter as tk
import matplotlib.pyplot as plt


class PlotHelper:
    def __init__(self, data_storage, log_text, canvas, fig):
        self.colors = ['#FF0000', '#0000FF', '#006400', '#F4A460', '#00FF7F', '#FF00FF']
        self.press = None
        self.split = True
        
        self.data_storage = data_storage
        self.log_text = log_text
        self.canvas = canvas
        self.fig = fig

        self.ax = None 


    def update_plot(self):
        self.data = self.data_storage.get_format()

        if self.split:
            # Clear the existing figure
            self.fig.clear()

            # Create 6 subplots when split=True
            self.ax = self.fig.subplots(2, 3)

            for i, ax_single in enumerate(self.ax.flat):
                col = f'R{i+1}({self.data_storage.res_name_conf[i]})'
                ax_single.plot(self.data['T'], self.data[col], marker='o', color=self.colors[i % len(self.colors)])  # Use i instead of idx for different colors
                ax_single.set_title(col)
                ax_single.set_xlabel('T')
                ax_single.set_ylabel('Values')
                ax_single.grid(True)

            plt.tight_layout()

        else:
            # Clear the existing figure
            self.fig.clear()
            self.ax = self.fig.add_subplot(111)

            # Plot all data in one plot when split=False
            for idx, column in enumerate(self.data.columns[1:]):
                self.ax.plot(self.data['T'], self.data[column], label=column, marker='o', color=self.colors[idx % len(self.colors)])
            
            self.canvas.mpl_connect('scroll_event', self.on_scroll)
            self.fig.canvas.mpl_connect('button_press_event', self.on_press)
            self.fig.canvas.mpl_connect('button_release_event', self.on_release)
            self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)


            self.ax.grid()
            self.ax.set_xlabel('T')
            self.ax.set_ylabel('Resistance')
            self.ax.legend()
            self.ax.set_title('Data Analysis')


        # Логи
        last_row = self.data.iloc[-1]

        self.log_text.insert(tk.END, f"Start series: {last_row._name}\n", "blue")
        for col in self.data.columns:
            val = last_row[col]
            self.log_text.insert(tk.END, f"{col}: {val}\n")
        self.log_text.insert(tk.END, f"end series\n", "blue")
        self.log_text.see(tk.END) 

        if last_row['T'] >= 350:
            self.canvas.get_tk_widget().xview_moveto(1)
        # Логи

        self.canvas.draw()

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

    def on_press(self, event, *args, **kwargs):
        if event.button == 2:  # Средняя кнопка мыши
            self.x0 = event.xdata
            self.y0 = event.ydata
            self.press = True

    def on_release(self, *args, **kwargs):
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