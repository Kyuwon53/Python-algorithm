def solution(N, M, K, numbers):
    # 배열의 크기 N, 숫자가 더해지는 횟수 M, 반복 제한 K
    result = 0
    numbers = sorted(numbers, reverse=True)
    first = numbers[0]
    second = numbers[1]

    cnt = 1

    while M > 0:
        if cnt > K:
            result += second
            cnt = 1
        else:
            result += first
            cnt += 1
        print(result)
        M -= 1

    return result
