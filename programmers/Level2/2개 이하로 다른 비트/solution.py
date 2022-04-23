def solution(numbers):
    # 비트 연산자 `^`를 사용하자
    # `^` : 두개를 비교하여 다르면 1을 반환
    answer = []
    for num in numbers:
        # 숫자를 4로 나눈 나머지가 3이 아닌 경우 +1
        if int(num) % 4 != 3:
            answer.append(num + 1)
        # 숫자를 4로 나눈 나머지가 3인 경우
        elif bin(num).count('1') == len(bin(num)[2:]):
            # 모든 숫자가 1로 이루어진 경우 11 => 101, 111 => 1011, 1111 => 10111
            result = num + 2 ** (len(bin(num)[2:]) - 1)
            answer.append(result)
        else:
            # 아닌 경우 01 -> 10으로 교체
            result = int('0b'+(bin(num)[::-1][:-2].replace('10','01',1))[::-1],2)
            answer.append(result)

    return answer

print(solution([11,10]))
