# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    for i in range(K):
        A = A[len(A) - 1:len(A)] + A[:len(A) - 1]

    return A
