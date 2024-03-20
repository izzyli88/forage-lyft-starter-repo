from Tires.Octoprime import Octoprime
import unittest


class OctoprimeTest(unittest.TestCase):
    def test_service_true(self):
        arr = [0, 0.1, 0.1, 2.8]
        tires = Octoprime(arr)
        self.assertTrue(tires.needs_service())

    def test_service_false(self):
        arr = [0, 0.1, 0.1, 0.1]
        tires = Octoprime(arr)
        self.assertFalse(tires.needs_service())