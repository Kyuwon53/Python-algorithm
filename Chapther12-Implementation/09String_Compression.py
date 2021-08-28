# 문자열 압축
# 2020 카카오 신입 공채
#  대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데,
#  문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와
#  반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
# 예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만,
# 2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다.
# 다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며,
# 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.
# 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로
# 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.
# 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
# 아이디어 : 1~ 문자열의 절반 길이 만큼 반복 => 처음부터 글자수 만큼 잘라서 비교
def solution(s):
    answer = len(s)
    length = len(s)//2
    for x in range(1,length+1):
        data = ""
        comp = s[0:x]
        cnt = 1
        for i in range(x,len(s),x):
            if comp == s[i: x + i]:
                cnt += 1
            else:
                data += str(cnt) + comp if cnt >=2 else comp
                comp = s[i: x+i]
                cnt = 1
        data += str(cnt) + comp if cnt >=2 else comp

        answer = min(answer, len(data))

    return answer

print(solution("ababcdcdababcdcd"))
