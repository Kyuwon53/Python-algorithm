def solution(arr1, arr2):
    answer = []
    for row in arr1:
        res_row = []
        for i in range(len(arr2[0])):
            res = 0
            for j in range(len(row)):
                res += row[j] * arr2[j][i]
            res_row.append(res)
        answer.append(res_row)

    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4], [2, 4], [3, 1]]
print(solution(arr1,arr2))
