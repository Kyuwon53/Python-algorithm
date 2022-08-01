from unittest import TestCase
from solution import solution


class Test(TestCase):
    def test_solution(self):
        self.assertEqual([3, 2, 2, 4, 2], solution(5, [3, 4, 4, 6, 1, 4, 4]))

