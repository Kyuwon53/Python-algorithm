from collections import deque


def solution(people, limit):
    answer = 0
    deq = deque(sorted(people))
    while deq:
        if len(deq) == 1:
            answer += 1
            break
        if deq[0] + deq[-1] <= limit:
            deq.pop()
            deq.popleft()
        else:
            deq.pop()
        answer += 1

    return answer


people = [40, 50, 150, 160]
limit = 200
print(solution(people, limit))
