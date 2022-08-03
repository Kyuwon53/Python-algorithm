from unittest import TestCase
from solution import solution


class Test(TestCase):
    def test_solution(self):
        S = "CAGCCTA"
        P = [2, 5, 0]
        Q = [4, 5, 6]
        self.assertListEqual([2, 4, 1],solution( S, P, Q))
