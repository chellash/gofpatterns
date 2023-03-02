import requests

class ConnectToInternet:
    def _init_(self):
        pass

    def connect(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class ConnectToWifi(ConnectToInternet):
    def _init_(self):
        super()._init_()

    def connect(self):
        print("Connecting to Wi-Fi...")
        # code to connect to Wi-Fi
        print("Connected to Wi-Fi")

class ConnectToMobileData(ConnectToInternet):
    def _init_(self):
        super()._init_()

    def connect(self):
        print("Connecting to mobile data...")
        # code to connect to mobile data
        print("Connected to mobile data")

def get_internet_connection(connection_type):
    if connection_type == "Wi-Fi":
        return ConnectToWifi()
    elif connection_type == "Mobile Data":
        return ConnectToMobileData()
    else:
        raise ValueError("Invalid connection type")

# Example usage
connection_type = "Wi-Fi"  # or "Mobile Data"
internet_connection = get_internet_connection(connection_type)
internet_connection.connect()

# Connect to the internet and fetch a web page
response = requests.get("https://www.example.com")
print(response.text)