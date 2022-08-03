# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    result = 0
    total = 0
    for a in A:
        if a == 0:
            total += 1
        else:
            result += total
    if result > 1000000000:
        result = -1
    return result
