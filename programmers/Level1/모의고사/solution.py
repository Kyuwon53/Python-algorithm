def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one_score = 0
    two_score = 0
    three_score = 0

    for i, j in enumerate(answers):
        if j == one[i % 5] :
            one_score += 1
        if j == two[i % 8] :
            two_score += 1
        if j == three[i % 10]:
            three_score += 1
    # print('one',one_score,'two',two_score,'three',three_score)
    return answer


print(solution([1,3,2,4,2]))
