from unittest import TestCase
import solution


class Test(TestCase):
    def test(self):
        self.assertEqual(solution.solution(6, 6, [
            [2, 2, 5, 4],
            [3, 3, 6, 6],
            [5, 1, 6, 3]
        ]), [8, 10, 25])

    def test_solution(self):
        queries = [
            [1, 1, 2, 2],
            [1, 2, 2, 3],
            [2, 1, 3, 2],
            [2, 2, 3, 3]
        ]

        self.assertEqual(solution.solution(3, 3, queries, [1, 1, 5, 3]))

    def test_solution1(self):
        queries = [
            [1, 1, 100, 97]
        ]

        self.assertEqual(solution.solution(3, 3, queries, [1]))
