import unittest
from solution import solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
        self.assertEqual(solution(s), [2, 1, 3, 4])

    def test_2(self):
        s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
        self.assertEqual(solution(s), [2, 1, 3, 4])

    def test_3(self):
        s = "{{20,111},{111}}"
        self.assertEqual(solution(s), [111, 20])

    def test_4(self):
        s = "{{123}}"
        self.assertEqual(solution(s), [123])

    def test_5(self):
        s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
        self.assertEqual(solution(s), [3, 2, 4, 1])


if __name__ == '__main__':
    unittest.main()
