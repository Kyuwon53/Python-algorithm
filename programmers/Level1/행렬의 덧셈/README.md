# 프로그래머스 - Level 1
## x만큼 간격이 있는 n개의 숫자
### 문제 설명
 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성
### 제한 사항
- 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

### 아이디어
- 행과 열 만큼 답변배열을 초기화
- 데이터값을 하나하나 연산 후 대입

### 개선사항
- Zip을 사용하여 더 간결하게 코딩할 수 있다.
```python
 answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
```

### [문제 출처](https://programmers.co.kr/learn/courses/30/lessons/12950)


