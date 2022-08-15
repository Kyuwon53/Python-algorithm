from unittest import TestCase
from solution import romanToInt


class TestSolution(TestCase):
    def test_roman_to_int3(self):
        self.assertEqual(3, romanToInt(self, "III"))

    def test_roman_to_int1994(self):
        self.assertEqual(1994, romanToInt(self, "MCMXCIV"))

    def test_roman_to_int58(self):
        self.assertEqual(58, romanToInt(self, "LVIII"))
