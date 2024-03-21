import serial, time, logging, threading

from src.DataBase.usb_read import get_avalibal_ports, UsbRead, speeds
from src.DataBase.test_data_gen import data_test_gen
from src.DataBase.data_stoarge import DataAnalyze

logging.basicConfig(filename='error.log', level=logging.ERROR)

class ProgState:
    def __init__(self) -> None:
        self.data_storage = DataAnalyze()
        self.avalibal_ports = get_avalibal_ports()
        self.avalibal_speeds = speeds

        self.is_reconect = False
        

        # Отвечает за физическое устройство 
        # Во время отладки может отвечать за виртуальный порт
        # Читает данные с порта
        self.usb_device = UsbRead()
        for port in self.avalibal_ports:   
            if self.usb_device.set_serial(port):
                break
            print('Доступные порты не найдены')
        
        # инициализация внутренего порта для разработки приложения
        # подключается к виртуальному порту, являясь средой для отображения данных
        # тупо кидает данные имитируя устройства иногда может принимать команды
        self.is_debug = False
        if self.is_debug:
            self.usb_device_debug = UsbRead()
            for port in self.avalibal_ports:   
                if self.usb_device_debug.set_serial(port):
                    break
            if not self.usb_device_debug.serial_device: print('Нет доступных портов для отладки')

        print(self.__dict__)

    def init_usb_thread(self, infinite=True, max_iterations=None, counter=0):
        """
        запускает поток чтения данных из трубы соединения UART
        """
        while infinite or (max_iterations is None or counter < max_iterations):
            # self.update_avalibal_ports()
            # if self.usb_device.serial_device is None or not self.usb_device.serial_device.is_open:
            #     print(f"{self.usb_device} port is not available. Exiting the loop.")
            #     break
            try:
                response = self.usb_device.read().strip()
                decoded_response = response
                print(decoded_response)
                self.data_storage.add_data(*map(int, decoded_response.split()))

            except (Exception, serial.SerialException) as e:
                try_reconect = self.init_reconnecting()
                if not try_reconect:
                    print(f"An error occurred: {e}")
                    logging.error(f"An error occurred: {e}")  # Log the error
                    # break  # Exit the loop on error

    def init_debug_usb_thread(self, infinite=True, max_iterations=None, counter=0):
        """
        запускает поток на основе тестовой генерации данных пихает их в virtual com port трубу
        """
        t = 10
        while infinite or (max_iterations is None or counter < max_iterations):
            self.update_avalibal_ports()
            print(self.avalibal_ports, 'wr')
            if self.usb_device_debug.serial_device is None or not self.usb_device_debug.serial_device.is_open:
                print(f"{self.usb_device_debug} port is not available. Exiting the loop.")
                break

            try:
                self.usb_device_debug.write(f'{str(data_test_gen(t))}\n'.encode("utf-8"))
                print(self.usb_device_debug.read().strip())
            except Exception as e:
                print(f"An error occurred: {e}")
                logging.error(f"An error occurred: {e}")  # Log the error
                break  # Exit the loop on error
    
    def update_avalibal_ports(self):
        self.avalibal_ports = get_avalibal_ports()

    def set_serial(self, port, speed=9600):
        self.usb_device.set_serial(port, speed=9600)

    def init_reconnecting(self, max_attempts=5, sleep_time=5):
        """
        Выполняет повторные попытки переподключения устройства.
        
        :param max_attempts: максимальное количество попыток
        :param sleep_time: время ожидания между попытками (в секундах)
        :return: True, если переподключение успешно, False в противном случае
        """
        attempt = 0

        while attempt < max_attempts:
            self.is_reconect = True
            print(f"Attempt reconnecting: {attempt+1}")
            self.update_avalibal_ports()
            print(self.avalibal_ports)
            for port in self.avalibal_ports:   
                if self.usb_device.set_serial(port):
                    self.is_reconect = False
                    return True
                print('Error: avalibal ports is not found')
            time.sleep(sleep_time)
            attempt += 1
        return False





# prog = ProgState()
# prog.init_usb_thread()