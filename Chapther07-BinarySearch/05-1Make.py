# 떡볶이 떡 만들기
# 떡의 개수 N, 떡의 길이 M
# 떡의 개별 높이
# 아이디어 : 가장 긴떡의 길이부터 탐색해서 절단기 높이보다 높은 떡을 잘라서 결과값에 더한다.
# 결과값이 고객이 원하는 떡의 길이(M)과 같으면 그 값을 리턴
n,m = map(int,input().split())
array = list(map(int,input().split()))
cnt = 0
result = 0
for i in range(max(array)-1,0,-1):
    if result == m:
        cnt = i+1
    result = 0
    for j in array:

        if i<j:
            result += j-i
print(cnt)
