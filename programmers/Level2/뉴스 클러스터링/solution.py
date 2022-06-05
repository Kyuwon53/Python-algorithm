import re


def solution(str1, str2):
    set1 = multi_set(str1)
    set2 = multi_set(str2)

    intersection_set = intersection(set1, set2)
    union_set = union(set1, set2)

    if len(union_set) != 0:
        return int(len(intersection_set) / len(union_set) * 65536)
    return int(1 * 65536)



def multi_set(target_str):
    result = []

    for i in range(len(target_str) - 1):
        target = target_str[i:i + 2].upper()
        if re.match("[A-Z]{2}", target) is not None:
            result.append(target)

    return result


def intersection(set1, set2):
    result = []
    target2 = list(set2)
    for s in set1:
        if s in target2:
            target2.pop(target2.index(s))
            result.append(s)

    return result


def union(set1, set2):
    result = list(set1)
    target2 = list(set2)
    for s in set1:
        if s in target2:
            target2.pop(target2.index(s))

    result += target2
    return result
