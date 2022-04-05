from collections import deque

def solution(prices):
    test = deque(prices)
    answer = []
    for i in range(len(prices)):
        time = 0
        test.popleft()

        for t in test:
            time += 1
            if prices[i] > t:
                break
        answer.append(time)

    return answer

