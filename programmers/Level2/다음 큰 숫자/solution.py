def solution(n):
    answer = n
    bin_num = format(n, 'b')
    cnt_one = bin_num.count('1')
    while True:
        answer += 1
        ans_one = format(answer,'b').count('1')
        if cnt_one == ans_one:
            break
    return answer

print(solution(78))
