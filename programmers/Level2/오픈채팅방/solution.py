def solution(record):
    answer = []
    user_info = {};
    for info in record:
        task = info.split(" ")
        status = task[0]
        user_id = task[1]
        if status == 'Enter':
            answer.append([user_id,"님이 들어왔습니다."])
            user_info[user_id] = task[2]
        if status == 'Leave':
            answer.append([user_id,"님이 나갔습니다."])
        if status == 'Change':
            user_info[user_id] = task[2]
    answer = list(map(lambda x : user_info[x[0]]+x[1], answer))

    return answer

record = ["Enter uid1234 Muzi"
        , "Enter uid4567 Prodo"
        ,"Leave uid1234"
        ,"Enter uid1234 Prodo"
        ,"Change uid4567 Ryan"]
print(solution(record))
