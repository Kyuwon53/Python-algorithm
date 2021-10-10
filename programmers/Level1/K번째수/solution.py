def solution(array, commands):
    answer = []
    arr = []
    for i in range(len(commands)):
        first = commands[i][0]-1
        end = commands[i][1]
        idx = commands[i][2]-1
        arr = array[first:end]
        answer.append(sorted(arr)[idx])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
