def solution(n):
    answer = 0
    for i in range(1,n//2):
        if (n // i) - (i // 2) + 1 < 1:
            break
        else:
            if i == 1:
                answer += 1
            elif i == 2 and n % 2 == 1:
                answer += 1
            elif i % 2 == 0 :
                if n == (n//i)*i+(i//2):
                    answer += 1
            elif i % 2 == 1 and n % i == 0:
                answer += 1

    return answer

print(solution(27))
