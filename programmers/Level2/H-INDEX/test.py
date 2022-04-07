import unittest
from solution import solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        citations = [3, 0, 6, 1, 5]
        self.assertEqual(solution(citations), 3)

    def test_2(self):
        citations = [10, 10, 10, 10, 10]
        self.assertEqual(solution(citations), 5)

    def test_3(self):
        citations = [0, 0, 0, 0, 0]
        self.assertEqual(solution(citations), 0)


if __name__ == '__main__':
    unittest.main()
