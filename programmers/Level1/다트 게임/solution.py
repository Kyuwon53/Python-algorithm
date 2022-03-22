def solution(dartResult):
    answer = 0
    scores = []
    bonus = {
        'S' : 1,
        'D' : 2,
        'T' : 3
    }
    before_dart = False
    for dart in dartResult:
        if dart.isdigit():
            if before_dart:
                score = scores.pop()
                dart = score * 10
            scores.append(int(dart))
            before_dart = True
        elif dart.isalpha():
            score = scores.pop()
            bonus_score = pow(score, bonus[dart])
            scores.append(bonus_score)
            before_dart = False
        elif dart == '*':
            if len(scores) == 1:
                current = scores.pop()
                scores.append(current * 2)
            else:
                current = scores.pop()
                before = scores.pop()
                scores.append(before * 2)
                scores.append(current * 2)
            before_dart = False
        elif dart == '#':
            score = scores.pop()
            scores.append(score * -1)
            before_dart = False

    answer = sum(scores)
    return answer

dartResult = '1D2S#10S'
print(solution(dartResult))
