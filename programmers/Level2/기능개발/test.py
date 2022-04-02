import unittest
from solution import solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        progresses = [93, 30, 55]
        speeds = [1, 30, 5]
        self.assertEqual(solution(progresses, speeds), [2, 1])

    def test_2(self):
        progresses = [95, 90, 99, 99, 80, 99]
        speeds = [1, 1, 1, 1, 1, 1]
        self.assertEqual(solution(progresses, speeds), [1, 3, 2])

    def test_3(self):
        progresses = [95, 95, 95, 95]
        speeds = [4, 3, 2, 1]
        self.assertEqual(solution(progresses, speeds), [2, 1, 1])

    def test_4(self):
        progresses = [20, 99, 93, 30, 55, 10]
        speeds = [5, 10, 1, 1, 30, 5]
        self.assertEqual(solution(progresses, speeds), [3, 3])


if __name__ == '__main__':
    unittest.main()
