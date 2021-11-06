def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for num in numbers:
        if num  == 0 :
            num = 11
        if num in (1,4,7):
            left = num
            answer += 'L'
        elif num in (3,6,9):
            right = num
            answer += 'R'
        elif num in (2,5,8,11):
            dleft = abs(num-left)
            dright = abs(num-right)
            dleft = (dleft//3) + (dleft%3)
            dright = (dright//3) + (dright%3)
            if dleft > dright :
                answer += 'R'
                right = num
            elif dright > dleft:
                answer += 'L'
                left = num
            else:
                if hand == 'right':
                    answer += 'R'
                    right = num
                elif hand == 'left':
                    answer += 'L'
                    left = num

    return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

print(solution(numbers, hand))
# 	"LRLLRRLLLRR"
