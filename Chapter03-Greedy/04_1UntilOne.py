# 어떠한 수 N이 1이 될 때까지
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다.
# 두 과정 중 하나를 반복적으로 선택하여 수행할 때 최소 횟수?

n,k = map(int,input().split())

cnt = 0

while n >= k:
    while n % k != 0:
        n-= 1
        cnt += 1
    n /= k
    cnt += 1
while n > 1:
    n-=1
    cnt += 1
print(cnt)