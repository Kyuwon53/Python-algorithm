import unittest
from solution import solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        brown = 10
        yellow = 2
        self.assertEqual(solution(brown, yellow), [4, 3])

    def test_2(self):
        brown = 8
        yellow = 1
        self.assertEqual(solution(brown, yellow), [3, 3])

    def test_3(self):
        brown = 24
        yellow = 24
        self.assertEqual(solution(brown, yellow), [8, 6])


if __name__ == '__main__':
    unittest.main()
