import unittest
from src.lab1.calculator import algorithm


class CalculatorTestCase(unittest.TestCase):

    def test_calculator(self):
        self.assertEqual(algorithm("500/(25+25)"), "10.0")


if __name__ == '__main__':
    unittest.main()
