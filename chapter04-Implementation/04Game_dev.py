
n,m = map(int,input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 캐릭터 현재 위치
x,y,direction = map(int,input().split())
# 현재 좌표 방문
d[x][y] = 1

# 전체 맵정보
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서 방향
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
# 왼쪽으로 회전 함수 , direction=> -1이면 서쪽이므로 3으로 변환
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
# 시작
count = 1
# 회전 횟수 , 4가 되면 모든 방향 확인이므로 한 칸 뒤로 이동
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤의 맵이 땅(0)일 경우 뒤로 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 바다(1)인 경우
        else:
            break
        turn_time = 0

print(count)