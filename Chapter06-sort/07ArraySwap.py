# A,B 두개의 배열, n개의 요소, 최대 k번 교환을 통해 A의 원소의 합의 최대값을 출력
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
# 아이디어 : a는 오름차순 정렬 ,b는 내림차순 정렬
# a의 왼쪽 , b는 오른쪽 데이터 비교하여 더 큰값을 a에 넣기
a.sort()
b.sort(reverse=True)
# 최대 k번 바꿀 수 있기 때문에 k번째 까지 비교하여 b의 데이터가 크면 a와 스왑
# a가 더 크면 그 이후 데이터도 a가 크기때문에 비교할 필요가 없다.
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i],a[i]
    else:
        break
print(sum(a))

