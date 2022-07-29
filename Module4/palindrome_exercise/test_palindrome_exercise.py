import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):

    def test_is_paindrome(self):
        self.assertTrue(is_palindrome('kajak'))
        self.assertTrue(is_palindrome('potop'))
        self.assertTrue(is_palindrome('aka'))
        self.assertTrue(is_palindrome('www'))

    def test_is_not_palindrome(self):
        self.assertFalse(is_palindrome('dom'))
        self.assertFalse(is_palindrome('terminator'))
        self.assertFalse(is_palindrome('alaska'))
        self.assertFalse(is_palindrome('example'))


if __name__ == '__main__':
    unittest.main()
