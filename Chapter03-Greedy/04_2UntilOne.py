# 어떠한 수 N이 1이 될 때까지
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다.
# 두 과정 중 하나를 반복적으로 선택하여 수행할 때 최소 횟수?

n,k = map(int,input().split())

cnt = 0

while True:
    # N이 K로 나누어떨어지는 수가 될 때까지 1빼기
    target = (n//k)*k   # n을 k로 나눈 몫에 k 곱
    cnt += n - target    # 나누어 떨어지는 수가 될 때까지 1뺀 횟수
    n = target
    if n < k:
        break
    n //= k
    cnt += 1
#마지막으로 남은 수
cnt += (n-1)
print(cnt)