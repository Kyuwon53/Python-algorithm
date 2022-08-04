from unittest import TestCase
from solution import solution


class Test(TestCase):
    def test_solution1(self):
        A = [10, 2, 5, 1, 8, 20]
        self.assertEqual(1, solution(A))

    def test_solution2(self):
        A = [10, 50, 5, 1]
        self.assertEqual(0, solution(A))
