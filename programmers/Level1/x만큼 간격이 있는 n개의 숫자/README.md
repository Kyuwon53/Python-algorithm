# 프로그래머스 - Level 1
## x만큼 간격이 있는 n개의 숫자
### 문제 설명
 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴

### 제한 사항
- x는 -10000000 이상, 10000000 이하인 정수입니다.
- n은 1000 이하인 자연수입니다.

### 아이디어
- for 문 사용

### 개선사항
- 더 간결한 식
    - ```python
        return [i * x + x for i in range(n)]
      ```
### [문제 출처](https://programmers.co.kr/learn/courses/30/lessons/12954)


