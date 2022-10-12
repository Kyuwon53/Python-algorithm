"""
문자열을 분리하고 분리된 개수를 출력
- 같은 문자끼리 하나의 집합
- 같은 문자라도 떨어져 있다면 다른 집합
스택으로 비교해서
다른 문자가 나올 때 1씩 올려준다.
"""


def count_split_set(sentence):
    if len(sentence) == 1:
        return 1
    count = 1
    before = sentence[0]
    for s in sentence[1:]:
        if before != s:
            count += 1
            before = s
    return count


def test_count_split_set():
    assert count_split_set("goorm") == 4
    assert count_split_set("algorithm") == 9


test_count_split_set()
