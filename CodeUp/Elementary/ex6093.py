n = int(input())
d = input().split()

for i in range(n):
    d[i] = int(d[i])

for i in range(n-1, -1, -1):
    print(d[i], end=' ')
