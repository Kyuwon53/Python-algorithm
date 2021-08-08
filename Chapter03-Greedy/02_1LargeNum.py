# 배열의 크기 N, 숫자가 더해지는 횟수 M, 더해질 수 있는 최대 횟수 K
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

# 데이터 정렬
data.sort()
# 가장 큰 수
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k): #가장 큰 수 k번 더하기
        if m == 0:
            break
        result += first
        m-=1
    if m == 0:
        break
    result += second
    m-= 1
print(result)
