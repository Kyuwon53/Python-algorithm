def solution(id_list, report, k):
    answer = []
    # 각 아이디에 (신고한 횟수, 신고 당한 횟수, 신고한 유저아이디 리스트 ) 딕셔너리 생성
    info_list = {id: [0, 0, []] for id in id_list}
    # 각 아이디에 이메일 횟수 배열 생성
    email_count = {id: 0 for id in id_list}

    for rep in report:
        reporter, receiver = rep.split()
        # 신고자가 신고한 유저아이디 리스트에 없을 경우 신고 당한 횟수 증가
        if not reporter in info_list[receiver][2]:
            info_list[receiver][1] += 1
            info_list[receiver][2].append(reporter)
        # 신고자는 신고한 횟수 증가
        info_list[reporter][0] += 1
    # 이메일 횟수 배열에 정지 기준을 넘은 사용자 +1 , 정지된 사용자를 신고한 유저아이디 +1
    for id in id_list:
        if info_list[id][1] >= k:
            email_count[id] + 1
            for reporter in info_list[id][2]:
                email_count[reporter] += 1

    for value in email_count.values():
        answer.append(value)
    return answer


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2

print(solution(id_list, report, k))
