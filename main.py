import threading
from tkinter import Tk

from src.prog_states import ProgState
from src.UI.main_page import StartPage


prog_state = ProgState()

def read_usb_thread():
    usb_thread = threading.Thread(target=prog_state.init_usb_thread)
    usb_thread.daemon = True
    usb_thread.start()


def main():
    read_usb_thread()
    window = StartPage(prog_state)  
    window.mainloop()

if __name__ == "__main__":
    print('ports:', prog_state.avalibal_ports)
    main()