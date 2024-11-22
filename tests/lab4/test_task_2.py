import unittest
from src.lab4.task2.main import main_str


class CalculatorTestCase(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(main_str(""), "")
