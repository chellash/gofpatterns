class MobilePhone:
    def _init_(self, factory):
        self.factory = factory

    def make_call(self, number):
        sim = self.factory.get_sim_card()
        sim.make_call(number)

class SimCard:
    def make_call(self, number):
        pass

class SingleSimCard(SimCard):
    def make_call(self, number):
        print(f"Making call from Single SIM card to {number}")

class DualSimCard(SimCard):
    def make_call(self, number):
        print(f"Making call from Dual SIM card to {number}")

class SimCardFactory:
    def get_sim_card(self):
        pass

class SingleSimCardFactory(SimCardFactory):
    def get_sim_card(self):
        return SingleSimCard()

class DualSimCardFactory(SimCardFactory):
    def get_sim_card(self):
        return DualSimCard()

if _name_ == "_main_":
    single_sim_factory = SingleSimCardFactory()
    dual_sim_factory = DualSimCardFactory()

    single_sim_phone = MobilePhone(single_sim_factory)
    dual_sim_phone = MobilePhone(dual_sim_factory)

    single_sim_phone.make_call("123456789")
    dual_sim_phone.make_call("987654321")