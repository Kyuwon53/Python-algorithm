from unittest import TestCase
from solution import solution


class Test(TestCase):
    def test_배열의_원소가_중간에_순서를_건너뛴_경우(self):
        A = [1, 3, 6, 4, 1, 2]
        self.assertEqual(5, solution(A))

    def test_배열의_원소가_모두_음수일_경우(self):
        A = [-1, -3]
        self.assertEqual(1, solution(A))

    def test_배열의_원소가_연속적일_경우(self):
        A = [1, 2, 3]
        self.assertEqual(4, solution(A))
