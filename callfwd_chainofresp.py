class CallHandler(object):
    def __init__(self, handler=None):
        self.handler = handler
        
    def handle_call(self, call):
        if self.handler:
            self.handler.handle_call(call)
        else:
            print("No handler available for call from {}".format(call.number))

class CallForwarder(CallHandler):
    def handle_call(self, call):
        if call.type == "forwarded":
            print("Forwarding call from {} to {}".format(call.number, call.forward_to))
        else:
            super().handle_call(call)

class JunkCallFilter(CallHandler):
    def handle_call(self, call):
        if call.number in self.junk_numbers:
            print("Blocking junk call from {}".format(call.number))
        else:
            super().handle_call(call)
            
    junk_numbers = ["111", "222", "333"]

class CallReceiver(CallHandler):
    def handle_call(self, call):
        print("Receiving call from {}".format(call.number))

class Call(object):
    def __init__(self, number, type, forward_to=None):
        self.number = number
        self.type = type
        self.forward_to = forward_to

# Usage
receiver = CallReceiver(CallForwarder(JunkCallFilter()))
receiver.handle_call(Call("123", "received"))
receiver.handle_call(Call("456", "forwarded", "789"))
receiver.handle_call(Call("111", "received"))
receiver.handle_call(Call("999", "received"))

# output
# Receiving call from 123
# Forwarding call from 456 to 789
# Blocking junk call from 111
# Receiving call from 999