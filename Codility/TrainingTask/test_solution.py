from unittest import TestCase
from solution import solution


class Test(TestCase):
    def 배열_순서가_빠짐없이_있을때(self):
        A = [4, 1, 3, 2]
        self.assertEqual(1, solution(A))

    def 배열의_원소_순서가_빠져있을때(self):
        A = [4, 1, 3]
        self.assertEqual(0, solution(A))

    def 배열의_원소가_중복되었을때(self):
        A = [4, 1, 3, 3, 2, 8]
        self.assertEqual(21, solution(A))
