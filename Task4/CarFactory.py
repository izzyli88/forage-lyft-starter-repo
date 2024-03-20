from Engine.CapuletEngine import CapuletEngine
from Engine.SternmanEngine import SternmanEngine
from Engine.WilloughbyEngine import WilloughbyEngine

from Battery.SpindlerBattery import SpindlerBattery
from Battery.NubbinBattery import NubbinBattery

from Tires.Carrigan import Carrigan
from Tires.Octoprime import Octoprime
from Car import Car


class CarFactory:
    @staticmethod
    def create_calliopse(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = Carrigan(tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = Carrigan(tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = Carrigan(tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = Octoprime(tire_wear)
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = Octoprime(tire_wear)
        return Car(engine, battery, tires)
