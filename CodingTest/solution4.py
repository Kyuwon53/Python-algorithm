def solution(n, info):
    answer = []
    lian = [0] * 11
    cnt = 0
    i = 0
    apeach = 0
    total = 0
    record = []
    while cnt - n < 0:
        lian[i] = info[i] + 1
        cnt += info[i] + 1
        i += 1
    # 총 점수
    for i in range(10):
        if info[i] != 0 or lian[i] !=0:
            if info[i] >= lian[i]:
                apeach += 10 - i
            else:
                total += 10 - i

    record.append([total-apeach,lian])
    print(cnt, lian)
    print(apeach,total)
    print(record)
    return answer


n = 5
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]

print(solution(n, info))
