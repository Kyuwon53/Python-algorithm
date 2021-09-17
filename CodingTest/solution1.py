def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    # repo_cnt : 신고당한 횟수  
    repo_cnt = [0 for i in range(len(id_list))]
    # stop_id : 정지된 아이디
    stop_id = []
    report_list = set(report)
    user_id = [[] for i in range(len(id_list))]    # 유저가 신고한 ID
    repo_id = []    # 신고당한 ID
    for repo in report_list:
        user_id[(id_list.index(repo.split()[0]))].append(repo.split()[1])
        repo_id.append(repo.split()[1])
        repo_cnt[id_list.index(repo.split()[1])] += 1 # 신고당한 횟수 카운트

    # 정지된 아이디 담기
    for idx in range(len(repo_cnt)):
        if repo_cnt[idx] >= k:
            stop_id.append(id_list[idx])

    for idx in range(len(id_list)):
        for id in stop_id:
            if user_id[idx].count(id)>0:
                answer[idx] += 1
    return answer

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
print(solution(id_list, report, 2))