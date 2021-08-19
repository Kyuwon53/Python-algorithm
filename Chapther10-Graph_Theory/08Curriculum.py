# 커리큘럼
# 선수 강의가 있는 강의는 선수 강의를 먼저 들어야만 해당 강의를 들을 수 있다.
# 총 N개의 강의를 듣고자한다. 모든 강의는 1번부터 N번까지의 번호를 가진다.
# 또한 동시에 여러 개의 강의를 들을 수 있다고 가정한다.
# 동빈이가 듣고자 하는 N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하시오

# 입력 : 첫째 줄에 듣고자 하는 강의의 수
#       다음  N개의 줄에는 강의시간, 선수강의 번호가 주어진다.
#       각 강의 번호는 1부터 N까지로 구성되며, 각 줄은 -1로 끝난다.
# 출력: N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력

# 리스트의 경우, 단순히 대입 연산을 하면 값이 변경될 때 문제가 발생할 수 있기 때문에, 리스트의 값을 복제해야 할 때는 deepcopy() 함수 사용

from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 집입차수는 0으로 초기화
indegree = [0]* (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 각 강의 시간을 0으로 초기화
time = [0] * (v+1)
# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]       # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1: -1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)        # 알고리즘 수행 결과를 담을 리스트
    q = deque()                         # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 집입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v+1):
        print(result[i])

topology_sort()
