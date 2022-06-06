def solution(arr):
    answer = []
    target = -1
    for num in arr:
        if target != num:
            answer.append(num)
        target = num

    return answer


print(solution([4, 4, 4, 3, 3]))
