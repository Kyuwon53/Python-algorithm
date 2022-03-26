import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    flag = False
    while len(scoville) >= 1:
        first = heapq.heappop(scoville)
        if first > K:
            flag = True
            break
        if len(scoville) >= 1:
            second = heapq.heappop(scoville)
            mix = first + (second * 2)
            heapq.heappush(scoville, mix)
            answer += 1

    if not flag:
        answer = -1
    return answer


scoville = [5, 3, 9, 10, 12]
k = 11
print(solution(scoville, k))
