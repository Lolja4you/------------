class Program:
    def __init__(self) -> None:
        self.is_init_usb = False
        self.load_settings() 
    
    def load_settings(self):...

    def save_settings(self):...

    def change_settings(self):...

    def default_settings(self):
        self.port = 'virtual_data'
        self.split = False
        self.reset = True
        self.defaul_resistors_name = [None,None,None,None,None,None]
        self.conf_format = "[%H:%M:%S %Y-%m-%d] "
        self.font = ('Helvetica', 10)
        self.is_mplcursors = True
    
    def init_usb_thread(self):...
    def destroy_usb_thread(self):...
