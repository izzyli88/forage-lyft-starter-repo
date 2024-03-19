from Phase2_Refactoring.Engine.CapuletEngine import CapuletEngine
from Phase2_Refactoring.Engine.SternmanEngine import SternmanEngine
from Phase2_Refactoring.Engine.WilloughbyEngine import WilloughbyEngine

from Phase2_Refactoring.Battery.SpindlerBattery import SpindlerBattery
from Phase2_Refactoring.Battery.NubbinBattery import NubbinBattery
from Phase2_Refactoring.Car import Car


class CarFactory:
    @staticmethod
    def create_calliopse(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
