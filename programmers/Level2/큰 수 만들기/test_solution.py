from unittest import TestCase
import solution


class Test(TestCase):
    def test_solution1(self):
        number = "1924"
        k = 2
        result = "94"
        self.assertEqual(solution.solution(number, k), result);

    def test_solution2(self):
        number = "1231234"
        k = 3
        result = "3234"
        self.assertEqual(solution.solution(number, k), result);

    def test_solution3(self):
        number = "4177252841"
        k = 4
        result = "775841"
        self.assertEqual(solution.solution(number, k), result);
