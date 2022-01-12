import math


def solution(n, a, b):
    answer = 0
    round = 1
    rounds = int(math.log2(n))
    for r in range(rounds):
        if a % 2 == 0:
            a = a//2
        elif a % 2 != 0:
            a = (a+1)//2
        if b % 2 == 0:
            b = b // 2
        elif b % 2 != 0:
            b = (b + 1) // 2

        if a == b :
            answer = round
            break
        round += 1

    return answer


print(solution(8, 4, 7))
