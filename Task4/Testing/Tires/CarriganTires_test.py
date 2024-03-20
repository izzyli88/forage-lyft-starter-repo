from Tires.Carrigan import Carrigan
import unittest

class CarriganTest(unittest.TestCase):
    def test_service_true(self):
        arr = [0, 0.1, 0.1, 0.9]
        tires = Carrigan(arr)
        self.assertTrue(tires.needs_service())
    
    def test_service_false(self):
        arr = [0, 0.1, 0.1, 0.1]
        tires = Carrigan(arr)
        self.assertFalse(tires.needs_service())