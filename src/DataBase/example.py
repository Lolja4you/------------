import serial, time

from src.DataBase.test_data_gen import data_test_gen

# Создаем объекты для COM1 и COM2
ser_com1 = serial.Serial('COM1', baudrate=1200, timeout=1)
ser_com2 = serial.Serial('COM2', baudrate=1200, timeout=1)

n = 50  # количество раз, которое вы хотите выполнить цикл
counter = 0

try:
    message = b"Hello, COM2! I'm COM1\n"

    # Отправляем сообщение с COM1 и читаем его на COM2
    
    while counter < n:
        data = str(data_test_gen())+'\n'
        ser_com1.write(data.encode("utf-8"))
        data_com2 = b''
        while True:
            byte = ser_com2.read(1)
            if byte == b'\n':  # Выход из цикла после получения полного сообщения
                break
            data_com2 += byte
        print("Message received on COM2:", data_com2.decode('utf-8'))

        counter+=1
        time.sleep(1)
except serial.SerialException as e:
    print("An error occurred:", e)

finally:
    ser_com1.close()
    ser_com2.close()


def reading_data_without_lenght(data):
    data_com2 = b''
    while True:
        byte = ser_com2.read(1)
        if byte == b'\n':  # Выход из цикла после получения полного сообщения
            break
        data_com2 += byte
    print("Message received on COM2:", data_com2.decode('utf-8'))






import serial, time, logging

from src.DataBase.usb_read import get_avalibal_ports, UsbRead
from src.DataBase.test_data_gen import data_test_gen


logging.basicConfig(filename='error.log', level=logging.ERROR)

data_read_port_1 = UsbRead()
data_write_port_2 = UsbRead()

data_read_port_1.set_serial('COM1', 9600)
data_write_port_2.set_serial('COM2', 9600)

n = 50
counter = 0

while counter < n:
    if data_read_port_1.serial_device is None or not data_read_port_1.serial_device.is_open:
        print("COM1 port is not available. Exiting the loop.")
        break

    if data_write_port_2.serial_device is None or not data_write_port_2.serial_device.is_open:
        print("COM2 port is not available. Exiting the loop.")
        break

    try:
        data_write_port_2.write(f'{str(data_test_gen())}\n'.encode("utf-8"))
        print(data_read_port_1.read().strip())
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")  # Log the error
        break  # Exit the loop on error

    counter += 1
    time.sleep(0.1)





import serial, time, logging

from src.DataBase.usb_read import get_avalibal_ports, UsbRead
from src.DataBase.test_data_gen import data_test_gen

logging.basicConfig(filename='error.log', level=logging.ERROR)

def process_serial_data(read_port, write_port, infinite=False, delay=0.1, max_iterations=None):
    counter = 0

    while infinite or (max_iterations is None or counter < max_iterations):
        if read_port.serial_device is None or not read_port.serial_device.is_open:
            print(f"{read_port} port is not available. Exiting the loop.")
            break

        if write_port.serial_device is None or not write_port.serial_device.is_open:
            print(f"{write_port} port is not available. Exiting the loop.")
            break

        try:
            write_port.write(f'{str(data_test_gen())}\n'.encode("utf-8"))
            print(read_port.read().strip())
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error(f"An error occurred: {e}")  # Log the error
            break  # Exit the loop on error

        counter += 1
        time.sleep(delay)

# Example of how to use the function with infinite input
data_read_port_1 = UsbRead()
data_write_port_2 = UsbRead()

data_read_port_1.set_serial('COM1', 9600)
data_write_port_2.set_serial('COM2', 9600)

if data_read_port_1.serial_device is None or not data_read_port_1.serial_device.is_open:
    print(f"{data_read_port_1} port is not available. Exiting the loop.")
    quit()

if data_write_port_2.serial_device is None or not data_write_port_2.serial_device.is_open:
    print(f"{data_write_port_2} port is not available. Exiting the loop.")
    quit()


try:
    process_serial_data(data_read_port_1, data_write_port_2, infinite=False)
except AttributeError:
    quit()