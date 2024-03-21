import subprocess

from serial.tools import list_ports, list_ports_windows

import sys, serial, glob

def get_avalibal_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns: 
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

speeds = [1200,2400, 4800, 9600, 19200, 38400, 57600, 115200]  
 
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR)

class UsbRead:
    def __init__(self):
        self.serial_device: object = None

    def set_serial(self, port, speed=9600):
        try:
            self.serial_device = serial.Serial(port, speed)
            return True
        except (OSError, serial.SerialException) as e:
            logging.error(f"Error setting serial port: {e}")
            return False

    def write(self, out):
        if self.serial_device:
            try:
                self.serial_device.write(out)
                return True
            except serial.SerialException as e:
                logging.error(f"Error writing to serial port: {e}")
                return e
        return False

    def read(self):
        if self.serial_device:
            try:
                return self.serial_device.readline().decode('utf-8')
            except serial.SerialException as e:
                logging.error(f"Error reading from serial port: {e}")
                return e
        return False

    def __del__(self):
        if self.serial_device:
            self.serial_device.close()