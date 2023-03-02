class PhoneCall:
    def _init_(self):
        self.duration = 0

    def dial(self, number):
        print(f"Calling {number}")
        self.duration = 10  # 10 seconds

    def end(self):
        print("Ending call")

class CallerTune(PhoneCall):
    def _init_(self, call):
        self._call = call

    def dial(self, number):
        self._call.dial(number)
        print("Playing caller tune")

    def end(self):
        self._call.end()

call = PhoneCall()
call = CallerTune(call)
call.dial("123-456-7890")
call.end()

# Output:
# Calling 123-456-7890
# Playing caller tune
# End