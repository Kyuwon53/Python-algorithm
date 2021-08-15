# 떡볶이 떡 만들기
# 떡의 개수 N, 떡의 길이 M
# 떡의 개별 높이
# 전형적인 이진 탐색 문제, 파라메트릭 서치 유형의 문제.
# 파라메트릭 서치: 최적화 문제를 결정 문제로 바꾸어 해결하는 기법 (원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제)

n,m = map(int,input().split())
array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start+end)//2
    for x in array:
        #잘랐을 때 떡의 양
        if x > mid:
            total += x -mid
    if total < m:   # 자른 떡의 양이 고객이 원하는 양보다 작다면 더 많이 잘라야 하므로 왼쪽 탐색
        end = mid - 1
    else: # 떡의 양이 충분하다면 덜 잘라야 하므로 오른쪽 탐색
        result = mid        # 최대한 덜 잘라야 되므로 결과에 저장
        start = mid + 1
print(result)