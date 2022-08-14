from unittest import TestCase
from solution import solution


class Test(TestCase):
    def test_solution(self):
        places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                  ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
        result = [1, 0, 1, 1, 1]
        self.assertEqual(result, solution(places))
