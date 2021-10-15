def solution(n):
    answer = 0
    a = [ i for i in range(n+1)]
    for i in range(2,n+1):
        if a[i] == 0:
            continue
        for j in range( 2 * i, n+1, i ):
            a[j] = 0
    for i in range(2, n+1):
        if a[i] != 0 :
            answer += 1
    return answer

print(solution(5))

