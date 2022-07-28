# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # numbers = []
    result = 0
    for a in A:
        result = result ^ a
        # if a in numbers:
        #     numbers.remove(a)
        # else:
        #     numbers.append(a)

    return result
