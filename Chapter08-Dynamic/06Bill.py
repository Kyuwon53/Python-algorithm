# N가지 종류의 화폐가 있다. 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
# 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
# 입력: n 화폐 종류 , m 가치의 합 => 공백으로 구분하여 입력, n개의 줄에 각 화폐 가치 입력
# 출력 : 경우의 수 ,불가능할 때는 -1을 출력한다.
n,m = map(int, input().split())
data =[]
for i in range(n):
    data.append(int(input()))
d= [10001]*(m+1)
d[0]=0
for i in range(n):
 for j in range(data[i], m+1):
     if d[j - data[i]] != 10001:
         d[j] = min(d[j], d[j - data[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

