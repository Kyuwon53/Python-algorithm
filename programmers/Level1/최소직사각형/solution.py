def solution(sizes):
    width = []
    height = []
    for size in sizes:
        width.append(max(size))
        height.append(min(size))
    return max(width)*max(height)

print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
