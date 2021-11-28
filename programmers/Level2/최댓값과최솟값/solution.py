def solution(s):
    answer = ''
    numbers = s.split()
    nums = []
    for num in numbers :
        nums.append(int(num))
    answer = str(min(nums)) + ' ' + str(max(nums))

    return answer

s = "1 2 3 4"
# "1 4"
print(solution(s))
