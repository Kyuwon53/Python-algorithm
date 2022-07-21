def solution(location):
    result = 0
    x = ord(location[0]) - 96
    y = int(location[1])

    steps = [
        [-2, -1],
        [-2, 1],
        [2, -1],
        [2, 1],
        [-1, -2],
        [-1, 2],
        [1, -2],
        [1, 2],
    ]

    for step in steps:
        next_x = x + step[0]
        next_y = y + step[1]
        if 1 <= next_x <= 8 and 1 <= next_y <= 8:
            result += 1

    return result
