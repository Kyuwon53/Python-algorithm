# 🔔 프로그래머스 - Level 1
## 📑 나누어 떨어지는 숫자 배열

### 📌 문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

### ✔️ 제한 사항
- arr은 자연수를 담은 배열입니다.
- 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
- divisor는 자연수입니다.
- array는 길이 1 이상인 배열입니다.

### 💡 아이디어
- 나누어 떨어지는 값을 배열에 담는다
- 배열에 담긴 값들을 정렬
- 배열에 담긴 값들이 없다면 -1 반환


### 💬 개선사항
- `sorted()` filter 기능을 활용하자


### 👉 문제 출처: [나누어 떨어지는 숫자 배열](https://programmers.co.kr/learn/courses/30/lessons/12910)


