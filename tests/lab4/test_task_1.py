import unittest
from src.lab4.task1.main import main


class TestRecommendations(unittest.TestCase):
    path_history = "../../src/lab4/task1/history.txt"
    path_films = "../../src/lab4/task1/films.txt"

    def test_main_with_positive(self):
        input_data = [1, 2, 3, 4, 5]
        expected_output = 'No recommend'
        self.assertEqual(main(input_data, TestRecommendations.path_history, TestRecommendations.path_films), expected_output)

    def test_main_with_many_numbers(self):
        input_data = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        expected_output = 'No recommend'
        self.assertEqual(main(input_data, TestRecommendations.path_history, TestRecommendations.path_films), expected_output)

    def test_main_with_mixed_numbers(self):
        input_data = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
        expected_output = 'Дюна'
        self.assertEqual(main(input_data, TestRecommendations.path_history, TestRecommendations.path_films), expected_output)

    def test_main_with_single_number(self):
        input_data = [100]
        expected_output = 'No recommend'
        self.assertEqual(main(input_data, TestRecommendations.path_history, TestRecommendations.path_films), expected_output)

    def test_main_with_empty_list(self):
        input_data = []
        expected_output = 'No recommend'
        self.assertEqual(main(input_data, TestRecommendations.path_history, TestRecommendations.path_films), expected_output)

    def test_main_with_floats(self):
        input_data = [10.5, 20.5, 30.5]
        expected_output = 'No recommend'
        self.assertEqual(main(input_data, TestRecommendations.path_history, TestRecommendations.path_films), expected_output)

    def test_main_with_negative(self):
        input_data = [-10.5, -20.5, -30.5]
        expected_output = 'No recommend'
        self.assertEqual(main(input_data, TestRecommendations.path_history, TestRecommendations.path_films), expected_output)

    def test_main_with_incorrect_type(self):
        input_data = ["-10.5", [-20.5], {-30.5}]
        expected_output = 'No recommend'
        self.assertEqual(main(input_data, TestRecommendations.path_history, TestRecommendations.path_films), expected_output)


if __name__ == '__main__':
    unittest.main()
