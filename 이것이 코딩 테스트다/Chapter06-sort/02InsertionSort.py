#작은 데이터를 만나면 그 자리에 멈춤 그전까지는 swap
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    for j in range(i, 0, -1): # i부터 0까지 탐색
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1],array[j]
        else:
            break
print(array)
