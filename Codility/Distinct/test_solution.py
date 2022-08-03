from unittest import TestCase
from solution import solution


class Test(TestCase):
    def test_solution(self):
        A = [2, 1, 1, 2, 3, 1]
        self.assertEqual(3, solution(A))
    def test_solution1(self):
        A = [2]
        self.assertEqual(1, solution(A))
    def test_solution2(self):
        A = [2,1,2,1,2]
        self.assertEqual(2, solution(A))
