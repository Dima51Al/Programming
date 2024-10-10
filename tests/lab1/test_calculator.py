import unittest

class CalculatorTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_one(self):
        self.assertEquals(1, 1)
    
    def test_calculator(self):
        self.assertEquals("1+1", "2")
