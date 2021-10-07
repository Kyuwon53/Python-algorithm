def solution(a, b):
    answer = (a + b) * (abs(b - a) + 1) // 2
    return answer


print(solution(5, 3))
