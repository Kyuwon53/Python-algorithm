def solution(s):
    answer = True
    pcnt = 0
    ycnt = 0
    for word in s:
        if word == 'p' or word == 'P':
            pcnt += 1
        if word == 'y' or word == 'Y':
            ycnt += 1
    if pcnt != ycnt:
        answer = False

    return answer

print(solution("Pyy"))
