from abc import ABC
from Engine import Engine
class WilloughbyEngine(Engine, ABC):
    MAX_MILES = 60_000

    def __init__(self, last_service_mileage, current_mileage):
        super().__init__()
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return self. current_mileage - self.last_service_mileage >= WilloughbyEngine.MAX_MILES