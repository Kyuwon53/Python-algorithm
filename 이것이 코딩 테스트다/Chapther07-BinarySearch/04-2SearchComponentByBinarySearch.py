# 부붐 찾기
# N개의 부품이 있고 각 부품마다 고유한 번호가 있다.
# M개 종류의 부품을 대량으로 구매한다고 할 때 가게 안에 부품이 모두 있는지 확인 하는 프로그램
# 손님이 요청한 부품 번호의 순서대로 확인해 있으면 yes, 없으면 no 출력
# 이진 탐색으로 찾기

def binary_Search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if target == array[mid]:
            return mid
        elif array[mid] > target:
            return binary_Search(array,target,start,mid-1)
        else:
            return  binary_Search(array,target,mid+1,end)

n = int(input())
array = list(map(int,input().split()))
array.sort()

m = int(input())
order = list(map(int,input().split()))

for i in order:
    result = binary_Search(array,i,0,n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
