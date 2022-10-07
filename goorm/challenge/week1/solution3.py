"""
최장 맨해튼 거리를 찾는 프로그램을 출력
(x1, y1) , (x2, y2)와 같이 좌표가 있을 때 , 맨해튼 거리는 |x1 - x2| + |y1 - y2|
4개의 정수를 2개씩 짝을 지어 좌표로 표현한다고 할 떄, 최장 맨해튼 거리를 찾는 프로그램을 출력
"""

numbers = list(map(int, input().split()))
sorted_number = sorted(numbers)
result = abs(sorted_number[0] - sorted_number[3]) + abs(sorted_number[1] - sorted_number[2])
print(result)