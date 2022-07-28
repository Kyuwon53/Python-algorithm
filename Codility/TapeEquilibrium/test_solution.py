from unittest import TestCase
import solution


class Test(TestCase):
    def test_solution(self):
        A = [3, 1, 2, 4, 3]
        self.assertEqual(solution.solution(A), 1)

    def test_solution1(self):
        A = [3, 3]
        self.assertEqual(solution.solution(A), 0)

    def test_solution2(self):
        A = [1, 13]
        self.assertEqual(solution.solution(A), 12)

    def test_solution3(self):
        A = [-11, 13]
        self.assertEqual(solution.solution(A), 24)

    def test_solution4(self):
        A = [11, -13]
        self.assertEqual(solution.solution(A), 24)