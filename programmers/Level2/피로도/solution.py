from itertools import permutations
def solution(k, dungeons):
    answer = -1
    nums = [k for k in range(len(dungeons))]
    perms = list(permutations(nums,len(dungeons)))
    result = [0 for i in range(len(perms))]
    for n,perm in enumerate(perms):
        temp = k
        for idx in perm:
            if temp >= dungeons[idx][0]:
                temp -= dungeons[idx][1]
                result[n] += 1
            else:
                break
    answer = max(result)
    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))
