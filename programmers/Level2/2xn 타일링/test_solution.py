from unittest import TestCase
import solution


class Test(TestCase):
    def test_solution(self):
        self.assertEqual(solution.solution(4), 5)
        self.assertEqual(solution.solution(5), 8)
