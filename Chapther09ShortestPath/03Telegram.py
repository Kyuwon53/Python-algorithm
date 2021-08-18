# N개의 도시가 있다. 각 도시는 보내고자 하는 메시지가 있는 경우
# 다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다.
# 하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치되어 있어야 한다.
# C에서 출발하여 최대한 많은 도시로 메시지를 보내고자 한다.
# C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산
# 입력:
# 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C
# 2~M+1 번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다. X->Y 가는데 시간 Z가 걸린다.
#  출력: 메시지를 받는 도시의 총 개수, 총 걸리는 시간
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
# 노드, 간선, 시작노드
n,m,start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)
# 모든 간선 정보 입력
for _ in range(m):
    x,y,z = map(int,input().split())
    # X->Y 가는데 시간 Z가 걸린다
    graph[x].append((y,z))

def dijkstra(start):
    q =[]
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count -1 을 출력
print(count-1, max_distance)

