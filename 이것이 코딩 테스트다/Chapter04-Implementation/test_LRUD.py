from unittest import TestCase
import LRUD


class Test(TestCase):
    def test_solution(self):
        n = 5
        route = ['R', 'R', 'R', 'U', 'D', 'D']
        self.fail(LRUD.solution(n, route))
