from unittest import TestCase
import Knight

class Test(TestCase):
    def test_solution(self):
        self.assertEqual(Knight.solution(location='a1'),2)
