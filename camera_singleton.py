class Camera:
    __instance = None

    def __init__(self):
        if Camera.__instance != None:
            raise Exception("This class is a singleton. Use Camera.getInstance() to get the instance.")
        else:
            Camera.__instance = self

    @staticmethod
    def getInstance():
        if Camera.__instance == None:
            Camera()
        return Camera.__instance

# Usage
camera1 = Camera.getInstance()
camera2 = Camera.getInstance()

print(camera1 is camera2) # True