"""
i가 소수인 Ai 값들을 합한 값을 출력한다.
1. 소수판별
2. 소수이면 합하기
"""
import math


def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def test_is_prime_number():
    assert not is_prime_number(1)
    assert is_prime_number(2)
    assert is_prime_number(3)
    assert not is_prime_number(4)
    assert is_prime_number(5)


test_is_prime_number()

x = int(input())
print(type(x))
numbers = list(map(int, input().split()))
result = 0
for i in range(x):
    if is_prime_number(i + 1):
        print(numbers[i])
        result += numbers[i]
print(result)
