from unittest import TestCase
from solution import solution


class Test(TestCase):
    def test_solution1(self):
        self.assertEqual(3, solution(6, 11, 2))

    def test_solution2(self):
        self.assertEqual(3, solution(1, 11, 3))

    def test_solution3(self):
        self.assertEqual(1, solution(1, 11, 7))

    def test_solution4(self):
        self.assertEqual(117647058, solution(1, 2000000000, 17))

    def test_solution5(self):
        self.assertEqual(20, solution(11, 345, 17))

    def test_solution6(self):
        self.assertEqual(1, solution(0, 0, 11))

    def test_solution7(self):
        self.assertEqual(0, solution(1, 1, 11))

    def test_solution8(self):
        self.assertEqual(0, solution(10, 10, 7))

    def test_solution9(self):
        self.assertEqual(2000000001, solution(0, 2000000000, 1))

    def test_solution10(self):
        self.assertEqual(2, solution(0, 2000000000, 2000000000))

    def test_solution11(self):
        self.assertEqual(1, solution(10, 10, 5))

    def test_solution12(self):
        self.assertEqual(0, solution(10, 10, 20))
