# https://www.acmicpc.net/problem/10825
# 학생의 성적을 정렬
# 1. 국어 점수가 감소하는 순서
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서
# 4. 모든 점수가 같으면 사전 순으로 증가 (단, 아스키코드에서 대문자는 소문자보다 작으므로 사전 순으로 앞에 온다.)

n = int(input())
score = []
for _ in range(n):
    score.append(input().split())
# sort함수 key 사용
score.sort(key=lambda x: (-int(x[1]), int(x[2]),-int(x[3]),x[0]))

for student in score:
    print(student[0])



