import unittest
from solution import solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        clothes1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
        self.assertEqual(solution(clothes1), 5)
        clothes2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
        self.assertEqual(solution(clothes2), 3)

if __name__ == '__main__':
    unittest.main()
