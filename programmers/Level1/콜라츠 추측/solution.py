def solution(num):
    answer = 0
    cnt = 0
    # 짝수이면 2로 나누기
    while num != 1:
        if cnt < 500 :
            if num % 2 == 0:
                num /= 2
                cnt += 1
            else:
                num = num * 3 + 1
                cnt += 1
            answer = cnt
        else:
            answer = -1
            break

    return answer

num = 626331
print(solution(num))
