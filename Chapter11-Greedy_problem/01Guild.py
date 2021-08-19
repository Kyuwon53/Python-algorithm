# 모험가 N명 ,공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있다.
# 최대 몇개의 모험가 그룹을 만들 수 있는가?
# N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값?

n = int(input())
data = list(map(int,input().split()))
data.sort()
group = 0       # 결성된 그룹 수
count = 0       # 그룹에 포함된 모험가 수
for i in data:
    count += 1
    if count >= i:  # 현재 그룹에 포함된 모험가 수가 공포도보다 높다면 새로운 그룹 생성
        group += 1  # 새로운 그룹 생성
        count = 0   # 새로운 그룹이 생성되었으므로 초기화

print(group)

