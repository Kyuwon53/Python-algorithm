# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A = sorted(A)
    # 삼각형 수가 있으면 1 없으면 0
    for i in range(2, len(A)):
        if A[i] < A[i - 1] + A[i - 2]:
            return 1
    return 0
