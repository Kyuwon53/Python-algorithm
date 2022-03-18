def solution(p):
    answer = ''
    if not p:
        return ''

    u, v = divide(p)

    if is_correct(u):
        return u + solution(v)

    else:
        answer += '('
        answer += solution(v)
        answer += ')'

        answer += translate(u)

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
        return temp


def divide(words):
    for i in range(2, len(words), 2):
        if is_balance(words[0:i]):
            return words[0:i], words[i:]
    return words, ''

def is_correct(words):
    stack = []
    for word in words:
        # 열림 괄호면 담고
        if word == '(':
            stack.append(word)
        # 닫힘 괄호이면
        else:
            # 스택이 비어있다면 열림괄호가 없는 상태이므로 올바른 괄호가 아님
            if not stack:
                return False
            # 스택이 안비어있다면 열림 괄호 pop
            stack.pop()
    return True

def is_balance(words):
    open_bracket = 0
    close_bracket = 0
    for word in words:
        if word == '(':
            open_bracket += 1
        elif word == ')':
            close_bracket += 1
        if open_bracket == close_bracket:
            return True
    return False


words = "(()())()"

print(solution(words))
