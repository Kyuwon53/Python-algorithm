import unittest
from solution import solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        prices = [1, 2, 3, 2, 3]
        self.assertEqual(solution(prices), [4, 3, 1, 1, 0])

    def test_2(self):
        prices = [5, 8, 6, 2, 4, 1]
        self.assertEqual(solution(prices), [3, 1, 1, 2, 1, 0])


if __name__ == '__main__':
    unittest.main()
