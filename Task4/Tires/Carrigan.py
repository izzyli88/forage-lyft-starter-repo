from Tires.Tires import Tires

class Carrigan(Tires):
    LIMIT = 0.9

    def __init__(self, tire_wear):
        super().__init__(tire_wear)

    def needs_service(self):
        for tire in self.tire_wear:
            if tire >= Carrigan.LIMIT:
                return True
        return False