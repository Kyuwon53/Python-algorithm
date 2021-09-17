import math
def solution(n, k):
    answer = -1
    # k진수로 바꾸기
    numeral = ''
    while n > 0:
        n, mod = divmod(n, k)
        numeral += str(mod)
    numeral = numeral[::-1]
    # 0을 기준으로 자르기
    prime_test = numeral.split('0')
    # 공백 문자열 제거
    prime_test = [i for i in prime_test if i]

    # 소수 판별 함수
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x))+1):
            print(i)
            # 소수가 아닐 경우
            if x % i == 0:
                return False
        return True

    cnt = 0
    for prime in prime_test:
        if is_prime(int(prime)):
            cnt += 1

    answer = cnt
    return answer


print(solution(437674, 3))
