def solution(numbers):
    answer = ''
    temp = [str(number) for number in numbers]
    temp.sort(key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(temp)))
    return answer


numbers = [0,0,0,0]
print(solution(numbers))
