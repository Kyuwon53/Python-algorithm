from unittest import TestCase
from solution import solution


class Test(TestCase):
    def test_solution1(self):
        A = [0, 1, 0, 1, 1]
        self.assertEqual(5, solution(A))

    def test_solution2(self):
        A = [0, 1, 1, 0, 0, 1, 1]
        self.assertEqual(8, solution(A))
