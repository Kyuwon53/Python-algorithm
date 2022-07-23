from unittest import TestCase
import solution


class Test(TestCase):
    def test_solution(self):
        orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
        course = [2, 3, 4]
        result = ["AC", "ACDE", "BCFG", "CDE"]
        self.assertEqual(solution.solution(orders, course), result)

    def test_solution2(self):
        orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
        course = [2, 3, 5]
        result = ["ACD", "AD", "ADE", "CD", "XYZ"]
        self.assertEqual(solution.solution(orders, course), result)

    def test_solution2(self):
        orders = ["XYZ", "XWY", "WXA"]
        course = [2, 3, 4]
        result = 	["WX", "XY"]
        self.assertEqual(solution.solution(orders, course), result)
