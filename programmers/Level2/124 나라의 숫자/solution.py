def solution(n):
    answer = ''
    three = ''
    while n > 0:
        n, mod = divmod(n, 3)
        if mod == 0:
            mod = 4
            n -= 1

        three += str(mod)

    answer = three[::-1]
    return answer


print(solution(10))
