from collections import deque


def solution(places):
    answer = []
    for place in places:
        p = [row for row in place]
        flag = True

        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    # 거리두기 안 지켰을 경우
                    if not bfs(i, j, p):
                        flag = False
            if not flag:
                break
        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer


def bfs(x, y, place):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * 5 for _ in range(5)]
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True

    while queue:
        x, y, cost = queue.popleft()
        if cost == 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                # 방문을 했다면 넘어간다.
                if visited[nx][ny]:
                    continue
                if place[nx][ny] == 'P':
                    return False
                # 책상인 경우 계속 탐색
                if place[nx][ny] == 'O':
                    queue.append((nx, ny, cost + 1))
                    visited[nx][ny] = True
    return True
