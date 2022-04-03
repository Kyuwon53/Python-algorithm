def solution(s):
    numbers = s.replace("{", "").replace("}", "")
    number_list = list(map(int, numbers.split(",")))
    de_dup = dict.fromkeys(number_list, 0)
    for key in de_dup:
        de_dup[key] += number_list.count(key)
    sorted_dict = sorted(de_dup.items(), key=lambda item: item[1], reverse=True)

    answer = [num[0] for num in sorted_dict]
    return answer
