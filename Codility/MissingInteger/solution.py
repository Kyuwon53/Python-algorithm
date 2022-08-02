# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # 배열에 없는 수 중 가장 작은 수
    # 배열의 크기만큼 확인 리스트를 만든다
    # 주어진 배열의 원소가 확인 리스트의 인덱스가 된다.
    check = [i + 1 for i in range(len(A))]
    dict = {}
    for a in A:
        dict[a] = a
    count = 0
    for num in check:
        if dict.get(num):
            count += 1
        else:
            return num

    result = count + 1 if count == len(A) else 1
    return result
