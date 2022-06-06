def solution(a, b):
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']  # 2016년 1월 1일은 금요일
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 4  # 1월 1일 금요일로 초기화
    for i in month[0:a - 1]:
        days += i
    days += b
    answer = day[days % 7]
    return answer


print(solution(5, 24))
