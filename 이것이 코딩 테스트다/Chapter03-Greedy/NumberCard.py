def solution(matrix):
    min_nums = []
    for row in matrix:
        min_nums.append(min(row))

    return max(min_nums)
