import math
import itertools


def solution(numbers):
    paper = [s for s in numbers]
    products = []
    for i in range(len(paper)):
        products += list(itertools.permutations(paper, i + 1))
    new_numbers = [int(''.join(product)) for product in products]
    print(new_numbers)

    prime_num = [i for i in new_numbers if is_prime_number(i)]
    return len(set(prime_num))


def is_prime_number(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
