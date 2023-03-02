class USB:
    def connect_usb(self):
        print("Connected to audio or video via USB")

class Bluetooth:
    def connect_bluetooth(self):
        print("Connected to audio or video via Bluetooth")

class Adapter:
    def __init__(self, device):
        self.device = device

    def connect(self):
        if isinstance(self.device, USB):
            self.device.connect_usb()
        elif isinstance(self.device, Bluetooth):
            self.device.connect_bluetooth()

usb = USB()
bluetooth = Bluetooth()

adapter_usb = Adapter(usb)
adapter_usb.connect()

adapter_bluetooth = Adapter(bluetooth)
adapter_bluetooth.connect()

# Output
# Connected to audio or video via USB
# Connected to audio or video via Bluetooth