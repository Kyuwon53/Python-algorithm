import unittest
from solution import solution

class MyTestCase(unittest.TestCase):
    def test_1(self):
        numbers = [2, 7]
        self.assertEqual(solution(numbers), [3, 11])

    def test_2(self):
        numbers = [3, 5]
        self.assertEqual(solution(numbers), [5, 6])

    def test_3(self):
        numbers = [11, 10]
        self.assertEqual(solution(numbers), [13, 11])

    def test_4(self):
        numbers = [15, 14, 12]
        self.assertEqual(solution(numbers), [23, 15, 13])

    def test_5(self):
        numbers = [343,779,891,421,222,256,512,128,100]
        self.assertEqual(solution(numbers), [347, 781, 893, 422, 223, 257, 513, 129, 101])

if __name__ == '__main__':
    unittest.main()
