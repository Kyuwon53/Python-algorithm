# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    check = [False for _ in A]
    n = len(A)
    total = n * (n + 1) // 2
    for a in A:
        if a > n:
            return 0
        if check[a - 1]:
            return 0
        check[a - 1] = True
        total -= a
    if total == 0:
        return 1
    else:
        return 0
