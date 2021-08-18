# 공중 미래 도시에는 1번부터 N번까지의 회사가 있는데 서로 도로를 통해 연결되어있다.
# 방문 판매원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다.
# 특정 회사와 다른 회사가 도로로 연결되어 있으면 정확히 1만큼의 시간으로 이동할 수 있다.
# A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤 X번 회사로 가는 것이 목표다.
# 방문 판매원이 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.

INF = int(1e9)
n, m = map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

# 자기자신으로 가는 그래프 0으로 초기화
for a in range(1,n+1):
    for b in range(1,m+1):
        if a==b:
            graph[a][b]=0
# 간선에 대한 정보 입력 , 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int,input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우
if distance >= INF:
    print("-1")
# 도달할 수 있다면, 최단 거리 출력
else:
    print(distance)
