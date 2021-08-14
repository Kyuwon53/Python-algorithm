# 이진탐색: 기본적으로 배열의 내부가 정렬 상태여야한다. 시작점,끝점, 중간점을 변수로 갖는다.
# 중간점을 기준으로 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 방법
# 시간복잡도 : O(logN)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2 #중간지점 시작점과 끝점을 나눈 몫
    if array[mid]==target:
        return mid
    elif array[mid] > target : #중간지점이 찾는 데이터보다 크다면 target은 mid의 왼쪽에 있다.
        return binary_search(array,target,start,mid-1)
    else: #중간점이 target보다 작은 경우 target은  mid의 오른쪽에 위치
        return binary_search(array,target,mid+1,end)
# 데이터 입력
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array,target,0,n-1)
if result == None:
    print('존재하지 않습니다.')
else:
    print(result + 1)
