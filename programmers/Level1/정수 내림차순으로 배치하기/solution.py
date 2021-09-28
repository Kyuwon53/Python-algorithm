def solution(n):
    answer = 0
    num =[]
    while n > 0 :
        num.append(n%10)
        n = n // 10
    num.sort(reverse=True)
    for i in num:
        if answer != 0:
            answer *= 10
        answer += i
    return answer

print(solution(118372))
