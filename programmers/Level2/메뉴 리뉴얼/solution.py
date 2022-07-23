import itertools
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        products = []
        for order in orders:
            for li in itertools.combinations(order, c):
                products.append(''.join(sorted(li)))
        counter = Counter(products).most_common()

        answer += [menu for menu, cnt in counter if cnt == counter[0][1] and cnt > 1]
    return sorted(answer)
