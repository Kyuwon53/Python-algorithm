import unittest
from solution import solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        people = [70, 50, 80, 50]
        limit = 100
        self.assertEqual(solution(people, limit), 3)

    def test_2(self):
        people = [70, 80, 50]
        limit = 100
        self.assertEqual(solution(people, limit), 3)

    def test_3(self):
        people = [40, 40, 50, 60, 70, 80]
        limit = 150
        self.assertEqual(solution(people, limit), 3)

    def test_4(self):
        people = [70, 50, 80, 50, 90, 40]
        limit = 240
        self.assertEqual(solution(people, limit), 3)

    def test_5(self):
        people = [40, 50, 150, 160]
        limit = 200
        self.assertEqual(solution(people, limit), 2)

    def test_6(self):
        people = [100, 500, 500, 900, 950]
        limit = 1000
        self.assertEqual(solution(people, limit), 3)


if __name__ == '__main__':
    unittest.main()
