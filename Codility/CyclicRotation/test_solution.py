from unittest import TestCase
import solution


class Test(TestCase):
    def test_solution_38976(self):
        A = [3, 8, 9, 7, 6]
        K = 3
        self.assertEqual(solution.solution(A, K), [9, 7, 6, 3, 8])

    def test_solution_000(self):
        A = [0, 0, 0]
        K = 1
        self.assertEqual(solution.solution(A, K), [0, 0, 0])

    def test_solution_000(self):
        A = [1, 2, 3, 4]
        K = 1
        self.assertEqual(solution.solution(A, K), [4, 1, 2, 3])

    def test_solution_000(self):
        A = [1, 2, 3, 4]
        K = 1
        self.assertEqual(solution.solution(A, K), [4, 1, 2, 3])
