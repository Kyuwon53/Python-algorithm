import unittest
from solution import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(solution(2,10,[7,4,5,6]), 8)


if __name__ == '__main__':
    unittest.main()
