from Engine.WilloughbyEngine import WilloughbyEngine
import unittest

class WilloughbyEngineTest(unittest.TestCase):
    def test_engine_service_true(self):
        engine = WilloughbyEngine(60_000, 120_000)
        self.assertTrue(engine.needs_service())

    def test_engine_service_false(self):
        engine = WilloughbyEngine(50_000, 50_000)
        self.assertFalse(engine.needs_service())