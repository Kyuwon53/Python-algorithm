from unittest import TestCase

import solution


class Test(TestCase):
    def test_solution_case1(self):
        str1 = "FRANCE"
        str2 = "french"
        self.assertEqual(solution.solution(str1, str2), 16384)

    def test_solution_case2(self):
        str1 = "handshake"
        str2 = "shake hands"
        self.assertEqual(solution.solution(str1, str2), 65536)

    def test_solution_case3(self):
        str1 = "aa1+aa2"
        str2 = "AAAA12"
        self.assertEqual(solution.solution(str1, str2), 43690)

    def test_solution_case4(self):
        str1 = "E=M*C^2"
        str2 = "e=m*c^2"
        self.assertEqual(solution.solution(str1, str2), 65536)

    def test_multiset(self):
        str1 = "FRANCE"
        str2 = "shake hands"
        str3 = "aa1+aa2"
        str4 = "E=M*C^2"
        str5 = "BAAAA"
        str6 = "AAA"

        self.assertEqual(solution.multi_set(str1), ["FR", "RA", "AN", "NC", "CE"])
        self.assertEqual(solution.multi_set(str2), ["SH", "HA", "AK", "KE", "HA", "AN", "ND", "DS"])
        self.assertEqual(solution.multi_set(str3), ["AA", "AA"])
        self.assertEqual(solution.multi_set(str4), [])
        self.assertEqual(solution.multi_set(str5), ['BA', 'AA', 'AA', 'AA'])
        self.assertEqual(solution.multi_set(str6), ['AA', 'AA'])

    def test_intersection(self):
        set1 = solution.multi_set("FRANCE")
        set2 = solution.multi_set("french")

        self.assertEqual(solution.intersection(set1, set2), ['FR', 'NC'])

        set3 = solution.multi_set("handshake")
        set4 = solution.multi_set("shake hands")

        self.assertEqual(solution.intersection(set3, set4), ['HA', 'AN', 'ND', 'DS', 'SH', 'HA', 'AK', 'KE'])

        set5 = solution.multi_set("BAAAA")
        set6 = solution.multi_set("AAA")

        self.assertEqual(solution.intersection(set5, set6), ['AA', 'AA'])

        set7 = solution.multi_set("aa1+aa2")
        set8 = solution.multi_set("AAAA12")

        self.assertEqual(solution.intersection(set7, set8), ['AA', 'AA'])

    def test_union(self):
        set1 = solution.multi_set("FRANCE")
        set2 = solution.multi_set("french")

        self.assertEqual(solution.union(set1, set2), ['FR', 'RA', 'AN', 'NC', 'CE', 'RE', 'EN', 'CH'])

        set3 = solution.multi_set("handshake")
        set4 = solution.multi_set("shake hands")

        self.assertEqual(solution.union(set3, set4), ['HA', 'AN', 'ND', 'DS', 'SH', 'HA', 'AK', 'KE'])

        set7 = solution.multi_set("aa1+aa2")
        set8 = solution.multi_set("AAAA12")

        self.assertEqual(solution.union(set7, set8), ['AA', 'AA','AA'])
