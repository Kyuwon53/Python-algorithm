# 성적이 낮은 순서로 학생 출력
n = int(input()) # 학생 수 입력
# ('학생이름',성적) 입력 받기
array = []
for i in range(n):
    # 공백으로 구분하여 0:학생이름, 1: 학생 성적 입력 받는다.
    input_data = input().split()
    array.append((input_data[0],input_data[1]))
# 성적을 key로 정렬
array = sorted(array, key=lambda student: student[1])
# 정렬 결과 출력
for student in array:
    print(student[0],end=' ')
    