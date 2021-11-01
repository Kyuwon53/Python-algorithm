def solution(n, arr1, arr2):
    answer = []
    res_arr1 = []
    res_arr2 = []
    for i in arr1:
        code = bin(i)[2:]
        if len(code) < n:
            code = '0'*(n-len(code)) + code

        result = ''
        for c in code:
            if c == '1' :
                result += '#'
            elif c == '0' :
                result += ' '
        res_arr1.append(result)
    for i in arr2:
        code = bin(i)[2:]
        if len(code) < n:
            code = '0'*(n-len(code)) + code

        result = ''
        for c in code:
            if c == '1' :
                result += '#'
            elif c == '0' :
                result += ' '
        res_arr2.append(result)
    for i in range(n):
        res_str =''
        for j in range(n):
            if res_arr1[i][j] == ' ' and res_arr2[i][j] == ' ':
                res_str += ' '
            else:
                res_str += '#'
        answer.append(res_str)
    return answer

n = 5
arr1 = 	[9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))
