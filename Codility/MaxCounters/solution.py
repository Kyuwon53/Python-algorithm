# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    result = [0 for _ in range(N)]
    max_num = 0
    cache = 0
    for a in A:
        if 1 <= a <= N:
            if result[a - 1] < cache:
                result[a - 1] = cache + 1
            else:
                result[a - 1] += 1

            if result[a - 1] > max_num:
                max_num = result[a - 1]

        if a == (N + 1):
            cache = max_num

    for i in range(N):
        if result[i] < cache:
            result[i] = cache
    return result
