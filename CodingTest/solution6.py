def solution(board, skill):
    answer = 0
    for step in skill:
        for row in range(step[1],step[3]+1):
            for col in range(step[2],step[4]+1):
                if step[0] == 1:
                    board[row][col] -= step[5]
                if step[0] == 2:
                    board[row][col] += step[5]

    for row in board:
        for i in range(len(row)):
            if row[i] > 0:
                answer += 1
    return answer

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board,skill))