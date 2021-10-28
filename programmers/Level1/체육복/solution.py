def solution(n, lost, reserve):
    n -= len(lost)
    lost.sort()
    reserve.sort()

    spare = []

    for i in lost:
        if i in reserve:
            reserve.pop(reserve.index(i))
            spare.append(i)
            n += 1
    for i in spare:
        lost.pop(lost.index(i))

    for i in lost:
        if i - 1 in reserve :
            reserve.pop(reserve.index(i-1))
            n += 1
        elif i + 1 in reserve :
            reserve.pop(reserve.index(i + 1))
            n += 1

    return n

n = 5
lost = [2,3,4]
reserve = [3,4,5]

print(solution(n, lost, reserve))
