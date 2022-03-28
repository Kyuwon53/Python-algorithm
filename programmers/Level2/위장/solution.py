def solution(clothes):
    cloth_dict = {cloth[1]: 0 for cloth in clothes}
    answer = 1
    for cloth in clothes:
        key = cloth[1]
        cloth_dict[key] += 1
    for value in cloth_dict.values():
        answer *= (value + 1)
    answer = answer - 1
    return answer


clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))
