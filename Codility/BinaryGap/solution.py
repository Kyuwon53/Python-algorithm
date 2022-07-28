def solution(N):
    binary = bin(N)[2:]
    count = 0
    result = 0
    for b in binary:
        if b == '0':
            count += 1
        else:
            result = max(result, count)
            count = 0

    return result
