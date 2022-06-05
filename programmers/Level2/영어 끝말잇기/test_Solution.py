from unittest import TestCase
import Solution


class Test(TestCase):
    def test_solution_case1(self):
        n = 3
        words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
        self.assertEqual(Solution.solution(n, words), [3, 3])

    def test_solution_case2(self):
        n = 5
        words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
        self.assertEqual(Solution.solution(n, words), [0, 0])

    def test_solution_case3(self):
        n = 2
        words = ["hello", "one", "even", "never", "now", "world", "draw"]
        self.assertEqual(Solution.solution(n, words), [1, 3])

    def test_has_word_case_true(self):
        word = 'tank'
        words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
        self.assertEqual(Solution.has_word(word, words), True)

    def test_has_word_case_false(self):
        word = 'table'
        words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
        self.assertEqual(Solution.has_word(word, words), False)

    def test_is_match_word_case_true(self):
        target = 'tank'
        current = 'kick'
        self.assertEqual(Solution.is_match_word(target, current), True)

    def test_is_match_word_case_false(self):
        target = 'tank'
        current = 'land'
        self.assertEqual(Solution.is_match_word(target, current), False)
