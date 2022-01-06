def solution(w,h):
    temp_w = w
    temp_h = h
    while(temp_h):
        temp = temp_w % temp_h
        temp_w = temp_h
        temp_h = temp
    gcd = temp_w
    answer = w * h - (w + h - gcd)
    return answer

print(solution(8,12))
