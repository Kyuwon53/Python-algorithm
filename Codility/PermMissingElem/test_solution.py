from unittest import TestCase
import solution


class Test(TestCase):
    def test_solution(self):
        A = [2, 3, 1, 5]
        self.assertEqual(solution.solution(A), 4)
