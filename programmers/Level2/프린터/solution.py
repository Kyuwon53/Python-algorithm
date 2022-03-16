def solution(priorities, location):
    # 1 2 3 4 5 6
    # 1 1 9 1 1 1
    # => 중요도가 9인 3 그다음 4 5 6 1 2

    # 1 2 3 4
    # 2 1 3 2
    # => 중요도 3인 3 그다음 4 그다음 1 => 3 4 1 2

    # 순서대로 스택에 담고 다음 요소의 숫자가 더 높으면 이전요소는 pop
    # 스택에 사이즈가 다 찰때까지 시행
    key = [i for i in range(len(priorities))]
    index = 0
    result = 0
    while priorities:
        current_value = priorities.pop(0)
        current_key = key.pop(0)
        flag = 0
        # 우선순위가 현재 값보다 크면 플래그 1
        for i in range(len(priorities)):
            if priorities[i] > current_value:
                flag = 1
        # 현재값의 우선순위가 더 높다면 현재 위치 이동
        if flag == 0:
            index += 1
            # 현재 키 값이 찾는 프린트와 같다면 키 값 반환
            if current_key == location:
                result = index
                return result
        # 우선순위가 작다면 순서를 뒤로 이동시킨다.
        else:
            priorities.append(current_value)
            key.append(current_key)
    return result

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))