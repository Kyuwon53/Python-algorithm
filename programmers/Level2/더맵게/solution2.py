from collections import deque


def solutiondeque(scoville, K):
    answer = 0
    mix = deque()
    scoville.sort()
    scov = deque(i for i in scoville)

    while (scov and scov[0] < K) or (mix and mix[0] < K):
        answer += 1
        if len(scov) + len(mix) <= 1:
            return -1
        foods = [0] * 2
        for idx in range(2):
            if scov and mix:
                foods[idx] = scov.popleft() if scov[0] < mix[0] else mix.popleft()
            elif scov:
                foods[idx] = scov.popleft()
            else:
                foods[idx] = mix.popleft()
        mix.append(foods[0] + foods[1] * 2)

    return answer
