def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i
    return n - 1


print(solution(12))
