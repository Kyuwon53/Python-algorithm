import unittest
from solution import solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        prices = [1, 2, 3, 2, 3]
        self.assertEqual(solution(prices),[])


if __name__ == '__main__':
    unittest.main()
