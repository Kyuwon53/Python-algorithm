def solution(arr):
    answer = []
    min_idx = arr.index(min(arr))
    arr.pop(min_idx)
    if len(arr) <= 0:
        answer.append(-1)
    else:
        answer = arr
    return answer

print(solution([4,3,2,1]))
