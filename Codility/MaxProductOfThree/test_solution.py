from unittest import TestCase
from solution import solution


class Test(TestCase):
    def test_solution(self):
        A = [-3, 1, 2, -2, 5, 6]
        self.assertEqual(60, solution(A))
