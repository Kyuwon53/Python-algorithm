def solution(board, moves):
    answer = 0
    N = len(board)
    doll = []
    for move in moves:
        cnt = 0
        for i in range(N):
            if board[i][move-1] != 0 and cnt == 0:
                idx = len(doll)
                if idx != 0:
                    if doll[idx - 1] == board[i][move - 1]:
                        doll.pop(idx-1)
                        answer += 2
                    else:
                        doll.append(board[i][move - 1])
                else:
                    doll.append(board[i][move-1])
                board[i][move - 1] = 0
                cnt += 1
            else:
                continue
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))
