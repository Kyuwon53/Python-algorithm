def solution(phone_book):
    answer = True
    phone_book.sort()
    phone = phone_book.pop(0)
    while phone_book:
        i = len(phone)
        if phone == phone_book[0][:i]:
            answer = False
            break
        phone = phone_book.pop(0)

    return answer

