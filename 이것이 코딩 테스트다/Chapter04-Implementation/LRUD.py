def solution(n, routes):
    # L (왼쪽), R(오른쪽), U(위) , D(밑)
    x = 1
    y = 1
    for route in routes:
        if route == 'L' and x > 1:
            x -= 1
        if route == 'R' and x < n:
            x += 1
        if route == 'U' and y > 1:
            y -= 1
        if route == 'D' and y < n:
            y += 1
    return 0
