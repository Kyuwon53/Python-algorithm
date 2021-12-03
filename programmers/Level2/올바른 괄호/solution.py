def solution(s):
    answer = True

    open = 0
    close = 0
    for i in range(len(s)) :
        if i == 0 and s[i:i+1] == ")":
            answer = False
        elif s[i:i+1] == "(":
            open += 1
        elif s[i:i+1] == ")":
            close -= 1
        if(open + close) < 0:
            answer = False
    if (open + close) != 0:
        answer = False
    return answer

s = ")()("

print(solution(s))
