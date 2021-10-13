def solution(arr):
    answer = []
    str = -1
    for num in arr :
        if str == num:
            continue
        elif str != num :
            answer.append(num)
        str = num

    return answer

print(solution([4,4,4,3,3]))
