def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0,0,0]

    for i, j in enumerate(answers):
        if j == one[i % 5] :
            scores[0] += 1
        if j == two[i % 8] :
            scores[1] += 1
        if j == three[i % 10]:
            scores[2] += 1

    for i, score in enumerate(scores):
        if score == max(scores):
            answer.append(i+1)
    return answer


print(solution([1,2,3,4,5]))
