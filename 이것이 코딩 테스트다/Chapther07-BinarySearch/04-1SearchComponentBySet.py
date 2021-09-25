# 부붐 찾기
# N개의 부품이 있고 각 부품마다 고유한 번호가 있다.
# M개 종류의 부품을 대량으로 구매한다고 할 때 가게 안에 부품이 모두 있는지 확인 하는 프로그램
# 손님이 요청한 부품 번호의 순서대로 확인해 있으면 yes, 없으면 no 출력
N = int(input())
component = set(map(int,input().split()))
m = int(input())
order = list(map(int,input().split()))

for i in order:
    if i in component:
        print('yes',end=' ')
    else:
        print('no', end=' ')
