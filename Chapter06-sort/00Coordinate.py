#직사각형 좌표구하기

def solution(v):
    answer = []
    x = v[0][0]
    y = v[0][1]
    if(x == v[1][0]):
        answer.append(v[2][0])
    elif(x ==v[2][0]):
        answer.append(v[1][0])
    else:
        answer.append(x)
    if (y == v[1][1]):
        answer.append(v[2][1])
    elif (x == v[2][1]):
        answer.append(v[1][1])
    else:
        answer.append(y)
    return answer

def solution2(v):
    answer=[]
    answer.append(v[0][0]^v[1][0]^v[2][0])
    answer.append(v[0][1]^v[1][1]^v[2][1])
    return answer
v=[[1,4],[3,4],[3,10]]

print("solution1: ",solution(v))
print("solution2: ",solution2(v))