def solution(s):
    answer = ''
    arr = s.split(' ')
    for i in range(len(arr)):
        alpha_list = list(arr[i])
        for cnt in range(len(alpha_list)):
            if cnt % 2 == 0:
                alpha_list[cnt] = alpha_list[cnt].upper()
            if cnt % 2 == 1:
                alpha_list[cnt] = alpha_list[cnt].lower()
        arr[i] = ''.join(alpha_list)
    answer = ' '.join(arr)
    return answer

print(solution("dfvsefsd  sdf we s "))
# "TrY HeLlO WoRlD"
