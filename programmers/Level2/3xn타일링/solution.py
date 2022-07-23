def solution(n):
    # 가로 길이가 2, 세로 길이가 1인 타일로
    # 가로 길이 n, 세로 길이가 3인 바닥을 채우는 방법
    # n 일 때의 경우의 수 => 이전 경우의 수 * 3 + 이전 경우의 수들의 특이 케이스들(각 2개) + n일 때 특이 케이스
    mod = 1000000007
    dp = [0 for i in range(n + 1)]
    dp[2] = 3
    if n > 2:
        dp[4] = 11
        for i in range(6, n + 1):
            dp[i] = dp[i - 2] * 3 + 2
            for j in range(i-4, -1, -2):
                dp[i] += dp[j] * 2
            dp[i] = dp[i] % mod

    return dp[n]
