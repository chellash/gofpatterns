class CallMediator:
    def __init__(self):
        self._calls = []

    def dial(self, call):
        for c in self._calls:
            if c.is_on_hold():
                c.resume()
            else:
                c.hold()
        self._calls.append(call)

    def disconnect(self, call):
        self._calls.remove(call)

    def hold(self, call):
        call.set_on_hold(True)

    def resume(self, call):
        call.set_on_hold(False)

    def add_call(self, call1, call2):
        call1.disconnect()
        call2.disconnect()
        new_call = Call(self, call1._number + " and " + call2._number)
        self.dial(new_call)

    def merge_call(self, call1, call2):
        call2.disconnect()
        call1._number += " and " + call2._number