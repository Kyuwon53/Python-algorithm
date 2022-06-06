def solution(s):
    start = (len(s) - 1) // 2
    end = len(s) // 2 + 1

    answer = s[start:end]

    return answer


print(solution("abcde"))
