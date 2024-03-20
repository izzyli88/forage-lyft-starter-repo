from abc import ABC, abstractmethod

class Tires(ABC):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear