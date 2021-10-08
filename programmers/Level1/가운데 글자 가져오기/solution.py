def solution(s):
    answer = ''
    s_len = len(s)
    # if len(s)%2 == 0:
    # answer = s[s_len // 2 - 1 : s_len // 2 + 1]
    answer = s[(s_len-1)//2:s_len//2+1]
    # else:
    #     answer = s[s_len//2:s_len//2+1]
    return answer

print(solution("abcde"))
