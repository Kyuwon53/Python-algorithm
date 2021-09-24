def solution(x):
    answer = True
    res = 0
    origin = x
    while x > 0:
        res += x%10
        x //= 10
    if (origin % res) != 0:
        answer = False
    return answer

print(solution(13))