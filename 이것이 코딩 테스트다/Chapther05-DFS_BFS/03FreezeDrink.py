# N x M 크기의 얼음 틀 , 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1
# 구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결된 것으로 간주

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x ,y):
    # 범위 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x -1, y) # 좌
        dfs(x,y -1)  # 하
        dfs(x +1,y) # 우
        dfs(x, y+1) # 상
        return True
    return False

#모든 노드(위치)에 대하여 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1

print(result)
