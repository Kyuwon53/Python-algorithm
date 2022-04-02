import math


def solution(progresses, speeds):
    remaining = [100 - progress for progress in progresses]
    work_times = []
    answer = []
    before = -1
    for i, speed in enumerate(speeds):
        pro = remaining[i]
        time = math.ceil(pro / speed)
        work_times.append(time)

    for work_time in work_times:
        if len(answer) == 0:
            answer.append(1)
            before = work_time
        else:
            if before >= work_time:
                answer[-1] += 1
            elif before < work_time:
                answer.append(1)
                before = work_time
    return answer
