def solution(n, m):
    answer = []
    for gcd in range(min(n,m),0,-1):
        if n % gcd == 0 and m % gcd == 0:
            answer.append(gcd)
            break
    for lcm in range(max(n,m),n*m+1):
        if lcm % n == 0 and lcm % m == 0:
            answer.append(lcm)
            break
    return answer

print(solution(2,5))
