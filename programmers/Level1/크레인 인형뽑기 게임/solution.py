def solution(board, moves):
    answer = 0
    N = len(board)
    doll = []
    for move in moves:
        for i in range(N):
            if board[i][move-1] != 0:
                doll.append(board[i][move - 1])
                board[i][move - 1] = 0
                if len(doll) > 1:
                    if doll[-1] == doll[-2]:
                        doll.pop(-1)
                        doll.pop(-1)
                        answer += 2
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))
