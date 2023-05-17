"""
경로의 개수
i번째 섬에 연결된 모든 다리는 i+1번 섬과 연결되어 있다.
섬 갯수만큼 다리 개수 입력 받아서 곱하기
"""
# def solution(n, str):
#     path = list(map(int,str.split()))
#     result = 1
#     for i in range(n):
#         result *= path[i]
#     return result
#
#
# def test_solution():
#     assert solution(3, "2 3 2") == 12
#     assert solution(3, "3 3 3") == 27
#     assert solution(10, "100 100 100 100 100 100 100 100 100 100") == 100000000000000000000
#
# test_solution()R

n = int(input())
bridges = list(map(int, input().split()))
result = 1
for i in range(n):
    result *= bridges[i]
print(result)
