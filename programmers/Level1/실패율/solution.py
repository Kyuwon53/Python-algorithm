import collections


def solution(N, stages):
    # 스테이지 수 만큼  배열 생성
    # 스테이지 배열에 담긴 수 까지 각 스테이지 카운트 업
    fail_count = collections.Counter(stages)
    fail_ratio = collections.defaultdict(float)
    fail_ratio[1] = len(stages)

    for i in range(1, N + 1):
        if fail_ratio[i] != 0:
            fail_ratio[i + 1] = fail_ratio[i] - fail_count[i]
            fail_ratio[i] = fail_count[i] / fail_ratio[i]

    if N + 1 in fail_ratio:
        del fail_ratio[N + 1]

    return sorted(fail_ratio, key=lambda x: -fail_ratio[x])


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))
