def solution(N, stages):
    answer = []
    clear = [0 for n in range(N+1)]
    fail_ratio = []
    people = len(stages)

    for stage in stages:
        # for s in range(1,stage):
        clear[stage-1] += 1
    clear.pop(N)
    for c in clear:
        fail_ratio.append(c/people)
        people -= c
    while len(answer) != N :
        for i, fail in enumerate(fail_ratio):
            # print(max(fail_ratio))
            if fail == max(fail_ratio):
                answer.append(i+1)
                fail_ratio[i] = 0

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))
