from unittest import TestCase
import solution


class Test(TestCase):
    def test_solution_1610612737(self):
        self.assertEqual(solution.solution(1610612737), 28)

    def test_solution_805306373(self):
        self.assertEqual(solution.solution(805306373), 25)

    def test_solution_6291457(self):
        self.assertEqual(solution.solution(6291457), 20)

    def test_solution_66561(self):
        self.assertEqual(solution.solution(66561), 9)

    def test_solution_51712(self):
        self.assertEqual(solution.solution(51712), 2)

    def test_solution_1162(self):
        self.assertEqual(solution.solution(1162), 3)

    def test_solution_328(self):
        self.assertEqual(solution.solution(328), 2)

    def test_solution_1024(self):
        self.assertEqual(solution.solution(1024), 0)

    def test_solution_1041(self):
        self.assertEqual(solution.solution(1041), 5)

    def test_solution_15(self):
        self.assertEqual(solution.solution(15), 0)

    def test_solution_32(self):
        self.assertEqual(solution.solution(32), 0)

    def test_solution_9(self):
        self.assertEqual(solution.solution(9), 2)

    def test_solution_529(self):
        self.assertEqual(solution.solution(529), 4)
