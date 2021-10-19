def solution(absolutes, signs):
    answer = 0
    for i, sign in enumerate(signs):
        if sign :
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

print(solution([1,2,3],[False,False,True]))
