n, name = input().split()
count = 0
for i in range(int(n)):
    target = input()
    if name in target:
        count += 1
print(count)

