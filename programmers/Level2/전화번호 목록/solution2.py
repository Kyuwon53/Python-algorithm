def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number[:-1]:
            temp += number
            if temp in hash_map:
                return False
    return True
