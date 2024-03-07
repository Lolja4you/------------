# import serial
# # Открываем Serial порт ('COMX' замените на имя вашего порта)
# ser = serial.Serial('COM7', 9600)
# # Читаем ответ от Arduino через Serial порт
# while True:
#     response = ser.readline()
#     decoded_response = response.decode('utf-8')
#     print(decoded_response)

import serial, threading, time, atexit

from src.DataAnalyze import DataAnalyze, data_test_gen
from src import StartPage


data_entrance_formater = DataAnalyze()

def read_usb():
    t = 10
    # ser = serial.Serial('COM7', 9600)
    
    while True:
        # Poduction
        # response = ser.readline()
        # decoded_response = response.decode('utf-8') 
        # data_entrance_formater.add_data(*map(int, decoded_response.split()))

        decoded_response = data_test_gen(t)
        t = decoded_response[0]
        data_entrance_formater.add_data(*decoded_response)
        time.sleep(1)

        

def start_usb_thread():
    usb_thread = threading.Thread(target=read_usb)
    usb_thread.daemon = True
    usb_thread.start()


def main():
    start_usb_thread()
    # start_UI_thread()

    window = StartPage(data_entrance_formater)
    window.mainloop()


def print_accumulated_data():
    data = data_entrance_formater.get_format()
    print("Accumulated Data:")
    print(data)


if __name__ == "__main__":
    # atexit.register(print_accumulated_data)
    main()

