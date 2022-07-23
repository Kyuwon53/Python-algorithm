def solution(rows, columns, queries):
    answer = []
    matrix = [[i + (j * columns) for i in range(1, columns + 1)] for j in range(rows)]
    for query in queries:
        # 시작과 끝 포인트 설정
        start_row = query[0] - 1
        start_col = query[1] - 1
        end_row = query[2] - 1
        end_col = query[3] - 1

        # 위, 아래, 왼쪽, 오른쪽 요소 추출
        top = [i for i in matrix[start_row][start_col:end_col]]
        bottom = [i for i in matrix[end_row][start_col + 1:end_col + 1]]
        left = [matrix[start_row + i][start_col] for i in range(end_row - start_row + 1)]
        right = [matrix[start_row + i][end_col] for i in range(end_row - start_row + 1)]
        # 위, 아래, 왼쪽, 오른쪽 요소 중 최솟값 추출

        answer.append(min(min(top), min(bottom), min(left), min(right)))

        # 회전
        # 왼쪽 -> 한 칸씩 위로
        # 오른쪽 -> 한 칸씩 아래로
        for index in range(len(top)):
            matrix[start_row][start_col + index + 1] = top[index]
        for index in range(len(bottom)):
            matrix[end_row][start_col + index] = bottom[index]
        for index in range(len(left) - 1):
            matrix[start_row + index][start_col] = left[index + 1]
        for index in range(len(right) - 1):
            matrix[start_row + index + 1][end_col] = right[index]

    return answer
