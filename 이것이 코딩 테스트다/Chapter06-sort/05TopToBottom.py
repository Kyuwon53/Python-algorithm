#수열을 내림차순으로 정렬하는 프로그램
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
array = sorted(array,reverse=True)  #내림차순으로 정렬

for i in array:
    print(i, end=' ')
    