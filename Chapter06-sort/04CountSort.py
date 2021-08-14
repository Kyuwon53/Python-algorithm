# 계수 정렬 : 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담기는 리스트에 데이터 값과 동일한 인덱스의 데이터를 증가시키는 정렬

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array) + 1) #모든 범위를 포함하는 리스트 선언(초기값 0)

for i in range(len(array)):
    count[array[i]]+= 1 #데이터에 해당하는 인덱스 값 증가

for  i in range(len(count)): # 리스트의 길이만큼
    for j in range(count[i]): # 해당 인덱스 값 만큼 출력
        print(i, end=' ')
