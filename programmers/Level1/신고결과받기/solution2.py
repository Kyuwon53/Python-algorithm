def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]

    # id : 신고 당한 횟수
    info_list = {id: 0 for id in id_list}
    # set으로 중복 제거 (신고자가 같은 사람을 두번 신고하면 1번으로 생각)
    for rep in set(report):
        # rep의 첫번째는 신고자 두번째는 신고 당한 사람
        # 신고 당한 횟수 증가
        info_list[rep.split()[1]] += 1

    # 이메일 횟수 배열에 정지 기준을 넘은 사용자 +1 , 정지된 사용자를 신고한 유저아이디 +1
    for rep in set(report):
        if info_list[rep.split()[1]] >= k:
            # 신고한 사람
            answer[id_list.index(rep.split()[0])] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "neo muzi", "muzi apeach"]
k = 2

print(solution(id_list, report, k))
