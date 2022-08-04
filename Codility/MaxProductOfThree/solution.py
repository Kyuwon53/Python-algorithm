# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A = sorted(A)

    minus_result = A[0] * A[1] * A[-1]
    plus_result = A[-1] * A[-2] * A[-3]
    return max(minus_result, plus_result)
