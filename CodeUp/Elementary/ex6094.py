# 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.
#
# 단,
# 첫 번째 번호와 마지막 번호가 몇 번인지는 아무도 모른다.
# 음수(-) 번호, 0번 번호도 있을 수 있다.

n = int(input())
k = input().split()

for i in range(n):
    k[i] = int(k[i])
print(min(k))

