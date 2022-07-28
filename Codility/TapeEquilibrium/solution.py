import math


def solution(A):
    front = 0
    back = sum(A)
    result = math.inf

    for i in range(len(A) - 1):
        front += A[i]
        back -= A[i]
        result = min(result, abs(front - back))

    return result
