# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    route = [0 for _ in range(X)]
    count = 0
    for i, a in enumerate(A):
        if route[a - 1] == 0:
            route[a - 1] = 1
            count += 1
        if count == X:
            return i
    return -1
