# 🔔 프로그래머스 - Level 1
## 📑 문자열 다루기
### 📌 문제 설명
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution
예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

### ✔️ 제한 사항
- s는 길이 1 이상, 길이 8 이하인 문자열입니다.


### 💡 아이디어
- 문자열 길이 검증
- isdigit 사용 

### 💬 개선사항
- 정규식 사용
```python
return bool(re.match("^(\d{4}|\d{6})$", s))
```
- 좀 더 간결한 식 
- `return s.isdigit() and len(s) in (4, 6)` 
### 👉 문제 출처: [문자열 다루기](https://programmers.co.kr/learn/courses/30/lessons/12918)


