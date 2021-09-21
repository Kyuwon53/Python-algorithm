import re
def solution(new_id):
    answer = ''
    answer = new_id.lower()
    answer = re.sub("[^a-z0-9\-\_\.]", '', answer)
    answer = re.sub('\.{2,}','.', answer)
    answer = re.sub('^\.|\.$','',answer)
    if(len(answer.replace(' ','')) == 0):
        answer = 'a'
    if(len(answer) >= 16):
        answer = answer[:15]
    answer = re.sub('^\.|\.$', '', answer)
    if(len(answer) <= 2):
        while len(answer) < 3:
            answer += answer[len(answer)-1:len(answer)]
    return answer


solution("...!@BaT#*..y.abcdefghijklm")
