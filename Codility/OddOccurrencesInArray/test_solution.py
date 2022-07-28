from unittest import TestCase
import solution


class Test(TestCase):
    def test_solution(self):
        A = [9, 3, 9, 3, 9, 7, 9]
        self.assertEqual(solution.solution(A), 7)

    def test_solution1(self):
        A = [9]
        self.assertEqual(solution.solution(A), 9)