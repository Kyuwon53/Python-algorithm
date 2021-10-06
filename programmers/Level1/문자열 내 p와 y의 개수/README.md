# 🔔 프로그래머스 - Level 1
## 📑 문자열 내 p와 y의 개수
### 📌 문제 설명
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

### ✔️ 제한 사항
- 문자열 s의 길이 : 50 이하의 자연수
- 문자열 s는 알파벳으로만 이루어져 있습니다.

### 💡 아이디어
- 받은 문자열을 p,P가 있으면 pcnt y,Y가 있으면 ycnt에 담아서 비교 

### 💬 개선사항
- 조건식을 더 간단히 하라 
```python
s.lower().count('p') == s.lower().count('y')
```
### 👉 문제 출처: [문자열 내 p와 y의 개수](https://programmers.co.kr/learn/courses/30/lessons/12916)


