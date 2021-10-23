def solution(nums):
    answer = 0
    pocket = len(set(nums))
    choose = len(nums)//2
    if choose > pocket:
        answer = pocket
    else:
        answer = choose
    return answer

print(solution([3,3,3,2,2,2]))
