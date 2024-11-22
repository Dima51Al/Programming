import unittest
from src.lab4.task2.main import main_str


class AgeGroupTestCase(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(main_str(""), "")


    def test_simply(self):
        self.assertEqual(main_str("John, 25"), "19-25: John (25)")

        self.assertEqual(main_str("Alice, 30"), "26-35: Alice (30)")

        self.assertEqual(main_str("Bob, 17"), "0-18: Bob (17)")

        self.assertEqual(main_str("алиса, 12"), "0-18: алиса (12)")

        self.assertEqual(main_str("Vlad, 124"), "")


    def test_incorrect_type(self):
        self.assertEqual(main_str(", 25"), "19-25:  (25)")

        self.assertEqual(main_str("Alice, 300"), "")

        self.assertEqual(main_str("Bob,, 17"), "")

        self.assertEqual(main_str("алиса, -12"), "")

        self.assertEqual(main_str("123, 00094"), "81-100: 123 (94)")


    def test_multy(self):
        input_data = """John, 25
        Alice, 30
        Bob, 17"""
        output_data = """0-18: Bob (17)
19-25: John (25)
26-35: Alice (30)"""
        self.assertEqual(main_str(input_data), output_data)


    def test_multy_with_incorrect_type(self):
        input_data = """John, 25
        Alice,, 30
        Bob, 17"""
        output_data = """0-18: Bob (17)
19-25: John (25)"""
        self.assertEqual(main_str(input_data), output_data)
        input_data = """John, 25
                Alice,, 30
                Bob, 17"""
        output_data = """0-18: Bob (17)
19-25: John (25)"""

        self.assertEqual(main_str(input_data), output_data)


if __name__ == '__main__':
    unittest.main()