from Battery.SpindlerBattery import SpindlerBattery
import unittest
import datetime

class SpindlerBatteryTest(unittest.TestCase):
    def test_battery_service_true(self):
        last_service = datetime.datetime(2021, 12, 12)
        current_date = datetime.datetime(2024, 12, 12)
        battery = SpindlerBattery(last_service, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_service_false(self):
        last_service = datetime.datetime(2021, 12, 12)
        current_date = datetime.datetime(2024, 12, 11)
        battery = SpindlerBattery(last_service, current_date)
        self.assertFalse(battery.needs_service())