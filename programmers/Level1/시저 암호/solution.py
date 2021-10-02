def solution(s, n):
    answer = ''
    for c in s:
        print(ord(c) + n)
        if ord(c) == 32:
            answer += ' '
        elif (ord(c) + n ) > 122 :
            answer += chr((ord(c) + n) - 26)
        elif  (ord(c) + n) > 90 and (ord(c)>=65 and ord(c) <= 90):
            answer += chr((ord(c) + n) - 26)
        else:
            answer += chr((ord(c) + n))
    return answer

# a 97 , z 122, A 65, Z 90
print(solution("a B z",4))
