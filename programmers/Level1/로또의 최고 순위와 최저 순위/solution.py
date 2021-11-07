def solution(lottos, win_nums):
    answer = []
    correct = 0
    miss = 0
    score = {6:1,5:2,4:3,3:4,2:5,1:6,0:6} 
    for lotto in lottos:
        if lotto in win_nums:
            correct += 1
        if lotto == 0:
            miss += 1
    max_score = score.get(correct + miss)
    min_score = score.get(correct)

    answer.append(max_score)
    answer.append(min_score)

    return answer

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]	

print(solution(lottos, win_nums))
