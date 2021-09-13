# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.
# 예시
# ...
# c = bool(int(a))
# d = bool(int(b))
# print((c and (not d)) or ((not c) and d))
#
# 참고
# 참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을 XOR(exclusive or, 배타적 논리합) 연산이라고도 부른다.
#
# 논리연산자는 사칙(+, -, *, /) 연산자와 마찬가지로 여러 번 중복해서 사용할 수 있는데,
# 사칙 연산자와 마찬가지로 계산 순서를 표시하기 위해 괄호 ( )를 사용할 수 있다.
# 괄호를 사용하면 계산 순서를 명확하게 표현할 수 있다.
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

