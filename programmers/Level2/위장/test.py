import unittest
from solution import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
        self.assertEqual(solution(clothes), 5)


if __name__ == '__main__':
    unittest.main()
