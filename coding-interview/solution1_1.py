def solution(sentence):
    strings = []
    for s in sentence:
        if s in strings:
            return True
        strings.append(s)
    return False


def test_solution():
    assert solution("abcasf")
    assert not solution("abcde")


test_solution()
