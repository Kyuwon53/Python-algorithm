def solution(s):
    answer = ''
    words = s.split(' ')

    for i, word in enumerate(words):
        if(not word[0:1].isdigit()):
            words[i] = word[0:1].upper()+word[1:].lower()
        else:
            words[i] = word.lower()
    answer = ' '.join(words)
    return answer

s = "3people unFollowed me"	#"3people Unfollowed Me"
#s = "for the last week"	#"For The Last Week"

print(solution(s))
