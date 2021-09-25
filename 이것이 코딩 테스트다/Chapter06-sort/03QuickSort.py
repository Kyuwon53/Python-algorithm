# 퀵 정렬 기준에 따라 큰 데이터와 작은 데이터를 교환하는 정렬
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: # ex) 0>9 ? end
        return
    # pivot(기준): 첫번째 데이터
    pivot = start
    left = start + 1 # 피벗을 기준으로 가장 첫번째 데이터
    right = end        # 피벗을 기준으로 가장 마지막 데이터
    while left <= right:
        while left <= end and array[left] <= array[pivot]: # 기준보다 큰 데이터 찾기
            left += 1
        while right > start and array[right] >= array[pivot]:  # 기준보다 작은 데이터 찾기
            right -= 1
        if left > right: # 엇갈리면 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot],array[right]
        else: # 엇갈린게 아니라면 교체 왼쪽은 피벗보다 작은 데이터가 오른쪽은 피벗보다 큰 데이터가 저장되어있다
            array[left], array[right]  = array[right] ,array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array,0,len(array)-1)
print(array)


# 퀵정렬 파이썬 특화 버전
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort_py(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 정렬이 끝난 것이므로 종료
    if len(array) <=1:
        return  array
    pivot = array[0] # pivot(기준)은 첫번째 데이터
    tail = array[1:] # pivot(기준)을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 왼쪽
    right_side = [x for x in tail if x >pivot] # 오른쪽

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)
print(quick_sort_py(array))
