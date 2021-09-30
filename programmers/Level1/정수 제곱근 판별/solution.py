import math
from math import sqrt


def solution(n):
    answer = 0
    num = sqrt(n)
    if num == math.floor(num):
        answer = int(math.pow(num + 1, 2))
    else:
        answer = -1
    return answer

print(solution(121))
