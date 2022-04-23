def solution(numbers):
    # 비트 연산자 `^`를 사용하자
    # `^` : 두개를 비교하여 다르면 1을 반환
    answer = []
    for num in numbers:
        flag = True
        index = 0
        while flag:
            index += 1
            target = int(num) + index
            count = str(bin(num ^ target)).count('1')
            if count == 1 or count == 2:
                flag = False
        answer.append(target)
    return answer

# print(solution([2,7]))