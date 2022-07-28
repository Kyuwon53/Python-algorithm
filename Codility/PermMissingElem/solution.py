# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n = len(A)
    correct_sum = (1 + n) * n // 2
    total = sum(A) - (n + 1)

    return correct_sum - total
