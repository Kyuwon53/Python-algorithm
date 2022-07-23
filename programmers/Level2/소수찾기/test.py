import unittest
from solution import solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        numbers = "17"
        self.assertEqual(solution(numbers), [1,7])


if __name__ == '__main__':
    unittest.main()
