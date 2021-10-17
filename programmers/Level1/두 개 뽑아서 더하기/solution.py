def solution(numbers):
    answer = []
    nums = set()
    for i,num in enumerate(numbers):
        for j in numbers[i+1:]:
            nums.update([num+j])
    for i in nums:
        answer.append(i)
    answer.sort()
    return answer

print(solution([5,0,2,7])) #[2,3,4,5,6,7]
