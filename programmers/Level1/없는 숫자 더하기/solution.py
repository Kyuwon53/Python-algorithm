def solution(numbers):
    answer = 0
    zero_ten = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        zero_ten[i] = 0

    answer = sum(zero_ten)
    return answer

print(solution([1,2,3,4,6,7,8,0]))
