def solution(brown, yellow):
    answer = []
    x_y_sum = int((brown - 4) / 2)
    for x in range(1, x_y_sum):
        y = x_y_sum - x
        xy = x * y
        if xy == yellow and x >= y:
            answer = [x + 2, y + 2]

    return answer
