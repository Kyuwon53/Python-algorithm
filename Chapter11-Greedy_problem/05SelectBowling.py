# 두 사람이 볼링을 치고 있다. 볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여된다.
# 같은 무게의 공도 서로 다른 공으로 간주한다.
# 볼링공의 무게는 1부터 M까지의 자연수 형태로 존재한다.
# 두 사람이 서로 무게가 다른 볼링공을 고르려 할 때 두 사람이 고를 수 있는 볼링공 번호의 조합을 구하시오
# 입력: 볼링공의 개수 N, 공의 최대무게 M (1<=M <=10)
#       볼링공의 무게 K가 공백으로 구분되어 순서대로

n, m = map(int, input().split())
k = list(map(int, input().split()))
cnt = 0
for i in range(m+1):
    if k.count(i) > 1:
        cnt += 1
result = int(n*(n-1)/2 - cnt)
print(result)

# 답안
# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11
for x in k:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m 까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i]   #무게가 i인 볼링공의 개수( A가 선택할 수 있는 개수) 제외
    result += array[i] * n  #B가 선택하는 경우의 수와 곱하기

print(result)
