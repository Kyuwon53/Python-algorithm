from unittest import TestCase
from solution import isPalindrome


class TestSolution(TestCase):
    def test_is_palindrome(self):
        self.assertEqual(False, isPalindrome(self, 1000021))
