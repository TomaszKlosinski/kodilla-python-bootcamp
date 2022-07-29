import unittest
from calculator import calculate


class TestPalindrome(unittest.TestCase):

    def test_calculate_addition(self) -> None:
        self.assertEqual(calculate("1", "2", "2"), 4.0)
        self.assertEqual(calculate("1", "2.3", "2"), 4.3)
        self.assertEqual(calculate("1", "2.3", "2.3"), 4.6)

    def test_calculate_subtraction(self) -> None:
        self.assertEqual(calculate("2", "5", "2"), 3.0)
        self.assertEqual(calculate("2", "5.3", "2"), 3.3)
        self.assertEqual(calculate("2", "5.4", "2.2"), 3.2)

    def test_calculate_multiplication(self) -> None:
        self.assertEqual(calculate("3", "2", "3"), 6.0)
        self.assertEqual(calculate("3", "2.3", "2"), 4.6)
        self.assertEqual(calculate("3", "2.3", "2.5"), 5.75)

    def test_calculate_division(self) -> None:
        self.assertEqual(calculate("4", "4", "2"), 2.0)
        self.assertEqual(calculate("4", "6.6", "2"), 3.3)
        self.assertEqual(calculate("4", "6.5", "2.5"), 2.6)


if __name__ == '__main__':
    unittest.main()
