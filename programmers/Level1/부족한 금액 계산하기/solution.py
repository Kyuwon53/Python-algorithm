def solution(price, money, count):
    answer = -1
    # total = 0
    # for i in range(1,count+1):
    #     total += price * i
    # answer = total - money
    # answer = price*((1 + count)*count // 2) - money
    # if answer < 0:
    #     answer = 0
    answer = max(0,price*((1 + count)*count // 2) - money)
    return answer

print(solution(3,20,4))     # 10
