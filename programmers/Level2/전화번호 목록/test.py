import unittest
from solution import solution;


class MyTestCase(unittest.TestCase):
    def test_1(self):
        phone_book = ["119", "97674223", "1195524421"]
        self.assertEqual(solution(phone_book), False)


if __name__ == '__main__':
    unittest.main()
