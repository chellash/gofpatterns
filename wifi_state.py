class NetworkState(object):
    def connect(self):
        pass
    
    def disconnect(self):
        pass

class WiFiConnectedState(NetworkState):
    def connect(self):
        print("The device is already connected to Wi-Fi.")
        
    def disconnect(self):
        print("Disconnecting from Wi-Fi.")
        return NoConnectionState()

class CellularDataState(NetworkState):
    def connect(self):
        print("The device is already connected to cellular data.")
        
    def disconnect(self):
        print("Disconnecting from cellular data.")
        return NoConnectionState()

class AirplaneModeState(NetworkState):
    def connect(self):
        print("The device is in airplane mode, cannot connect to any network.")
        
    def disconnect(self):
        print("The device is already in airplane mode.")

class NoConnectionState(NetworkState):
    def connect(self):
        print("Connecting to Wi-Fi.")
        return WiFiConnectedState()
        
    def disconnect(self):
        print("The device is already disconnected.")

class MobilePhone(object):
    def __init__(self):
        self.state = NoConnectionState()

    def connect(self):
        self.state = self.state.connect()

    def disconnect(self):
        self.state = self.state.disconnect()

# Usage
mobile_phone = MobilePhone()
mobile_phone.connect()
mobile_phone.connect()
mobile_phone.disconnect()
mobile_phone.disconnect()

# output
# Connecting to Wi-Fi.
# The device is already connected to Wi-Fi.
# Disconnecting from Wi-Fi.
# The device is already disconnected.