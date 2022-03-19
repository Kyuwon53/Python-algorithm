def solution(N, stages):
    # 스테이지 수 만큼  배열 생성
    fail_count = [0] * N
    fail_ratio = []
    player = len(stages)

    # 스테이지 배열에 담긴 수 까지 각 스테이지 카운트 업
    for stage in stages:
        if stage > N:
            continue
        fail_count[stage - 1] += 1

    for i, count in enumerate(fail_count):
        fail_ratio.append([i, (count / player)])
        player -= count

    fail_ratio.sort(key=lambda x: (-x[1], x[0]))
    answer = [fail[0] + 1 for fail in fail_ratio]

    return answer