from unittest import TestCase

import solution


class Test(TestCase):
    def test_solution_case_normal(self):
        str1 = "FRANCE"
        str2 = "french"
        self.assertEqual(solution.solution(str1, str2), 16384)

    def test_solution_case_공백_포함(self):
        str1 = "handshake"
        str2 = "shake hands"
        self.assertEqual(solution.solution(str1, str2), 65536)

    def test_solution_case_숫자_특수문자_포함(self):
        str1 = "aa1+aa2"
        str2 = "AAAA12"
        self.assertEqual(solution.solution(str1, str2), 43690)

    def test_solution_case_다중집합_존재하지않음(self):
        str1 = "E=M*C^2"
        str2 = "e=m*c^2"
        self.assertEqual(solution.solution(str1, str2), 65536)

    def test_multiset_case_normal(self):
        test_string = "FRANCE"
        self.assertEqual(solution.multi_set(test_string), ["FR", "RA", "AN", "NC", "CE"])

    def test_multiset_case_공백_포함(self):
        test_string = "shake hands"
        self.assertEqual(solution.multi_set(test_string), ["SH", "HA", "AK", "KE", "HA", "AN", "ND", "DS"])

    def test_multiset_case_숫자_특수문자_포함(self):
        test_string = "aa1+aa2"
        self.assertEqual(solution.multi_set(test_string), ["AA", "AA"])

    def test_multiset_case_다중집합_존재하지않음(self):
        test_string = "E=M*C^2"
        self.assertEqual(solution.multi_set(test_string), [])

    def test_multiset_case_중복된_문자열(self):
        test_string = "BAAAA"
        self.assertEqual(solution.multi_set(test_string), ['BA', 'AA', 'AA', 'AA'])

    def test_intersection_normal(self):
        set1 = solution.multi_set("FRANCE")
        set2 = solution.multi_set("french")

        self.assertEqual(solution.intersection(set1, set2), ['FR', 'NC'])

    def test_intersection_case_교집합과_다중집합이_같은_경우(self):
        set1 = solution.multi_set("handshake")
        set2 = solution.multi_set("shake hands")

        self.assertEqual(solution.intersection(set1, set2), ['HA', 'AN', 'ND', 'DS', 'SH', 'HA', 'AK', 'KE'])

    def test_intersection_case_다른집합이_또다른집합의_부분집합인_경우(self):
        set1 = solution.multi_set("BAAAA")
        set2 = solution.multi_set("AAA")

        self.assertEqual(solution.intersection(set1, set2), ['AA', 'AA'])

    def test_intersection_case_다중집합이_서로_같은_경우(self):
        set1 = solution.multi_set("aa1+aa2")
        set2 = solution.multi_set("AAAA12")

        self.assertEqual(solution.intersection(set1, set2), ['AA', 'AA'])

    def test_union_normal(self):
        set1 = solution.multi_set("FRANCE")
        set2 = solution.multi_set("french")

        self.assertEqual(solution.union(set1, set2), ['FR', 'RA', 'AN', 'NC', 'CE', 'RE', 'EN', 'CH'])

    def test_union_합집합과_다중집합이_같은_경우(self):
        set1 = solution.multi_set("handshake")
        set2 = solution.multi_set("shake hands")

        self.assertEqual(solution.union(set1, set2), ['HA', 'AN', 'ND', 'DS', 'SH', 'HA', 'AK', 'KE'])

    def test_union_다른집합이_또다른집합의_부분집합인_경우(self):
        set1 = solution.multi_set("aa1+aa2")
        set2 = solution.multi_set("AAAA12")

        self.assertEqual(solution.union(set1, set2), ['AA', 'AA', 'AA'])

    def test_union_case_다중집합이_서로_같은_경우(self):
        set1 = solution.multi_set("aa1+aa2")
        set2 = solution.multi_set("AAAA12")

        self.assertEqual(solution.intersection(set1, set2), ['AA', 'AA'])
