from Tires.Tires import Tires

class Octoprime(Tires):
    LIMIT = 3

    def __init__(self, tire_wear):
        super().__init__(tire_wear)

    def needs_service(self):
        sum_service = 0.0
        for tire in self.tire_wear:
            sum_service += tire
        return sum_service >= Octoprime.LIMIT
