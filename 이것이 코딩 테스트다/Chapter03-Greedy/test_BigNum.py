from unittest import TestCase
import BigNum


class Test(TestCase):
    def test_solution(self):
        N = 5
        M = 8
        K = 3
        numbers = [2, 4, 5, 4, 6]
        self.assertEqual(BigNum.solution(N, M, K, numbers), 46)
