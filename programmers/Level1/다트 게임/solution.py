def solution(dartResult):
    answer = 0
    ind = 0
    for dart in dartResult:
        if dart == 'S':
            ind = 1
            answer += pow(num, ind)
        elif dart == 'D':
            ind = 2
            answer += pow(num, ind)
        elif dart == 'T':
            ind = 3
            answer += pow(num, ind)
        elif dart == '*':
            answer *= 2
        elif dart == '#':
            answer += pow(num, ind) *(-1) *2
        elif dart == '0' and num == 1:
            num *= 10
        else:
            num = int(dart)

    return answer

dartResult = '1T2D3D#'
print(solution(dartResult))
