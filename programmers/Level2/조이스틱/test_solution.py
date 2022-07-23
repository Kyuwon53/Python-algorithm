from unittest import TestCase
import solution


class Test(TestCase):
    def test_solution(self):
        self.assertEqual(solution.solution("JEROEN"), 56)
        self.assertEqual(solution.solution("JAN"), 23)
        self.assertEqual(solution.solution("JAZ"), 11)
