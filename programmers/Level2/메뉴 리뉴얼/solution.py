def solution(orders, course):
    answer = []
    menu = {}
    for ascii in range(65,91):
        alpha = chr(ascii)
        menu[alpha] = 0
    for order in orders:
        for dish in order:
            menu[dish] += 1
    sort_by_value = sorted(menu.items(), key=lambda x: x[1], reverse=True)

    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(orders, course))
