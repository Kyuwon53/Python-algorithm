# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
# 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,
#
# 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

h, w = input().split()
graph = [[0 for i in range(int(w))] for j in range(int(h))]

n = int(input())
for i in range(n):
    l, d, x, y = input().split()
    for j in range(int(l)):
        if int(d) == 0:
            graph[int(x)-1][int(y)+j-1] = 1
        else:
            graph[int(x)-1+ j][int(y)-1] = 1

for i in range(int(h)):
    for j in range(int(w)):
        print(graph[i][j],end=' ')
    print()