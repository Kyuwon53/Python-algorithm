def solution(n, lost, reserve):
    n -= len(lost)
    for i in lost:
        if i in reserve:
            reserve.pop(reserve.index(i))
            # lost.pop(lost.index(i))
            n += 1

    for i in lost:
        if i - 1 in reserve :
            reserve.pop(reserve.index(i-1))
            n += 1
        elif i + 1 in reserve :
            reserve.pop(reserve.index(i + 1))
            n += 1

    return n

n = 8
lost = [1,2,4,6]
reserve = [1,2,4,6]

print(solution(n, lost, reserve))
