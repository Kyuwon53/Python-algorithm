# 개선된 다익스트라 알고리즘
# 시간복잡도 최악의 경우에도 O(ElogV)를 보장하여 해결
# V: 노드의 개수, E: 간선의 개수
# 힙의 자료구조를 사용.
# 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리
# 힙 자료구조는 우선순위 큐를 구현하기 위하여 사용하는 자료구조
# 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제
# 최소 힙 구조 : 값이 낮은 데이터가 먼저 삭제
# 최대 힙 구조 : 값이 큰 데이터가 먼저 삭제
# 큐 라이브러리에 데이터의 묶음을 넣으면, 첫 번째 원소를 기준으로 우선순위를 설정한다.
# 파이썬 : 최소 힙 구조
# => 최소 힙을 최대 힙처럼 사용하기 위해 일부러 우선순위에 해당하는 값에 음수 부호(-)를 붙여서 넣었다가,
# 나중에 우선순위 큐에서 꺼낸 다음에 다시 음수 부호(-)를 붙여서 원래의 값으로 돌리는 방식도 자주 쓴다.

# 다익스트라 최단 경로 알고리즘에 우선순위 큐를 이용해서 시작 노드로부터 '거리'가 짧은 노드 순서대로 큐에서 나올 수 있도록
# 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용
# 앞의 코드의 get_smallest_node()라는 함수를 작성할 필요가 없다.
# 최단 거리가 가장 짧은 노드를 선택하는 과정을 다익스트라 최단 경로 함수 안에서 우선순위 큐를 이용

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n+1)

# a번 노드에서 b번 노드로 가는 비용이 c라는 의미
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

