# import serial
# # Открываем Serial порт ('COMX' замените на имя вашего порта)
# ser = serial.Serial('COM7', 9600)
# # Читаем ответ от Arduino через Serial порт
# while True:
#     response = ser.readline()
#     decoded_response = response.decode('utf-8')
#     print(decoded_response)

from src.DataAnalyze import DataAnalyze, data_test_gen



def main():
    data_entrance_formater = DataAnalyze()
    
    import time, mplcursors
    import matplotlib.pyplot as plt

    start_time = time.time()
    t = 10
    plt.figure(figsize=(10, 6))
    plt.ion()  # Включаем интерактивный режим

    def on_close(event):
        plt.close()
        raise SystemExit


    while True:
        data_input = data_test_gen(t)
        t = data_input[0]
        data_entrance_formater.add_data(*data_input)

        plt.clf()  # Очищаем предыдущий график
        for column in data_entrance_formater.get_format().columns[1:]:
            plt.plot(data_entrance_formater.get_format()['T'], data_entrance_formater.get_format()[column], label=column, marker='o')

        mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f"({sel.target[0]}, {sel.target[1]})"))

        plt.grid()
        plt.xlabel('T')
        plt.ylabel('Value')
        plt.legend()
        plt.title('Data Analysis')
        plt.draw()
        plt.pause(1.5)  # Пауза для обновления графика
        fig = plt.gcf()
        fig.canvas.mpl_connect('close_event', on_close)
if __name__ == "__main__":
    main()
