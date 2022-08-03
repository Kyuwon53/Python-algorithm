# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) == 0:
        return 0

    count = 1
    sort = sorted(A)
    curr = sort[0]

    for i in range(1, len(A)):
        if curr != sort[i]:
            count += 1
        curr = sort[i]
    return count
