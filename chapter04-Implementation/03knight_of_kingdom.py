# 현재 나이트의 위치 입력
input_data = input()
# 행
row = int(input_data[1])
# 열 (문자를 수로 변환)
col = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트 이동 방향
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)
