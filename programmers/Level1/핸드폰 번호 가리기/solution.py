def solution(phone_number):
    answer = ''
    phone_len = len(phone_number) - 4
    answer = '*' * phone_len+phone_number[phone_len:]
    return answer

print(solution("01033334444"))