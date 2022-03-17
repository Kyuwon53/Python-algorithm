def solution(p):
    answer = ''
    if len(p) == 0:
        return answer
    temp = p
    while not is_correct(p):
        u, v = seperator(temp)
        if is_correct(u):
            answer += u
            if is_correct(v):
                answer += v
            else:
                temp = v
        else:
            u = translate(u)
        temp = u + v
        if is_correct(temp):
            p = temp
            answer = p
    return answer


def translate(words):
    if len(words) == 0:
        return ''
    else:
        temp = words[1:-1]
        temp = temp.replace('(', '0')
        temp = temp.replace(')', '1')
        temp = temp.replace('0', ')')
        temp = temp.replace('1', '(')
        return '(' + temp + ')'


def seperator(p):
    for i in range(0, len(p), 2):
        if is_correct(p[0:i]):
            u = p[0:i]
            v = p[i:]
        if len(u) == 0 and is_correct(p[i:]):
            u = p[0:i]
            v = p[i:]
    return u, v


def is_correct(words):
    stack = []
    for word in words:
        # 스택이 비어있으면 담기
        if len(stack) == 0:
            stack.append(word)
        else:
            current = stack.pop()
            if current == word or (current == ')' and word == '('):
                stack.append(current)
                stack.append(word)

    if len(stack) == 0:
        return True
    else:
        return False


def is_balance(words):
    right_bracket = 0
    left_bracket = 0

    if len(words) == 0:
        return True

    for word in words:
        if "(" == word:
            left_bracket += 1
        if ")" == word:
            right_bracket += 1

    if right_bracket == left_bracket:
        return True
    else:
        return False


p = "(()())()"
print(solution(p))
