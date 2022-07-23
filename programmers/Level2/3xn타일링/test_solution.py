from unittest import TestCase
import solution

class Test(TestCase):
    def test_solution(self):
        self.assertEqual(solution.solution(4),11)
        self.assertEqual(solution.solution(6), 41)
