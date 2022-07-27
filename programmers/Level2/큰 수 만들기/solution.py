from collections import deque


def solution(number, k):
    stack = deque();
    for i in number:
        while stack and stack[-1] < i and k > 0:
            k -= 1
            stack.pop()
        stack.append(i)
    return ''.join(stack)
