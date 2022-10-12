n, k = map(int, input().split())
result = 0
for _ in range(k):
    x, y = map(int, input().split())
    total = 5
    if x == 1:
        total -= 1
    if x == n:
        total -= 1
    if y == 1:
        total -= 1
    if y == n:
        total -= 1
    result += total
print(result)
