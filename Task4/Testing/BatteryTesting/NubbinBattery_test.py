from Battery.NubbinBattery import NubbinBattery
import unittest
import datetime

class NubbinBatteryTest(unittest.TestCase):
    def test_service_true(self):
        last_service = datetime.datetime(2018, 12, 12)
        current_date = datetime.datetime(2024, 12, 12)
        battery = NubbinBattery(last_service, current_date)
        self.assertTrue(battery.needs_service())

    def test_service_false(self):
        last_service = datetime.datetime(2018, 12, 12)
        current_date = datetime.datetime(2022, 12, 11)
        battery = NubbinBattery(last_service, current_date)
        self.assertFalse(battery.needs_service())
