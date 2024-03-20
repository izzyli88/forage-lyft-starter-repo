from Engine.CapuletEngine import CapuletEngine
import unittest

class CapuletTest(unittest.TestCase):
    def test_capulet_service_true(self):
        capulet = CapuletEngine(90_000, 120_000)
        self.assertTrue(capulet.needs_service())

    def test_capulet_service_false(self):
        capulet = CapuletEngine(90_000, 119_999)
        self.assertFalse(capulet.needs_service())
