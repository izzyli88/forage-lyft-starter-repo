from Engine.SternmanEngine import SternmanEngine
import unittest

class SternmanEngineTest(unittest.TestCase):
    def test_engine_service_true(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_engine_service_false(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())