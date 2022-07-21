from unittest import TestCase
import NumberCard


class Test(TestCase):
    def test_solution(self):
        self.assertEqual(NumberCard.solution(matrix=[[3, 1, 2], [4, 1, 4], [2, 2, 2]]), 2)
        self.assertEqual(NumberCard.solution(matrix=[[7, 3, 1, 8], [3, 3, 3, 4]]), 3)
