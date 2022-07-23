from builtins import enumerate


def solution(name):
    answer = 0
    move = len(name) - 1
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        next_index = i + 1
        while next_index < len(name) and name[next_index] == 'A':
            next_index += 1
        move = min(move, 2 * i + len(name) - next_index, 2(len(name) - next_index) + i)
    return answer + move
