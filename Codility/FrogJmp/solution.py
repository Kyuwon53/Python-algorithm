# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # X 위치에서 D 만큼씩 점프해서 Y 보다 크거나 같은 횟수
    distance = Y - X
    count = distance // D + (1 if distance % D > 0 else 0)
    return count
