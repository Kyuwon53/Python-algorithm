def solution(n):
    answer = 0
    three = []
    while n > 0:
        three.append(n % 3)
        n //= 3
    print(three)
    for i, num in enumerate(three[::-1]):
        answer += num * 3 ** i
    return answer

print(solution(125))
