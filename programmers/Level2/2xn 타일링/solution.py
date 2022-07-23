def solution(n):
    # 가로 길이가 2, 세로 길이가 1인 타일로
    # 가로 길이 n, 세로 길이가 3인 바닥을 채우는 방법
    # f(n) = f(n-1) + f(n-2)
    mod = 1000000007
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 2

    if n > 2:
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] = dp[i] % mod
    return dp[n - 1]
