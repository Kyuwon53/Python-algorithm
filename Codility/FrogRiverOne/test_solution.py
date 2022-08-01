from unittest import TestCase
import solution


class Test(TestCase):
    def test_solution(self):
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        self.assertEqual(6,solution.solution(5, A))
