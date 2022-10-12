"""
t: 시험의 개수
합격: 매 시험 성적의 평균보다 이상인 사람
합격자 수 a, 응시자 수 b => a/b 로 표기
"""


def print_test_result():
    for _ in range(2):
        b = int(input())
        scores = list(map(int, input().split()))
        total = 0
        for score in scores:
            total += score
        avg = total / b

        pass_cnt = 0
        for score in scores:
            if score >= avg:
                pass_cnt += 1
        return str(pass_cnt) + "/" + str(b)


n = int(input())
result = []
for _ in range(n):
    result.append(print_test_result())

for r in result:
    print(r)
