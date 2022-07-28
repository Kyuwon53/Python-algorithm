from unittest import TestCase
import solution


class Test(TestCase):
    def test_solution(self):
        self.assertEqual(solution.solution(10, 85, 30),3)

    def test_solution1(self):
        self.assertEqual(solution.solution(10, 50, 20),2)

    def test_solution2(self):
        self.assertEqual(solution.solution(70, 80, 20),1)

    def test_solution3(self):
        self.assertEqual(solution.solution(70, 70, 20),0)