def solution(n, words):
    used_words = [words[0]]

    for word in words[1:]:
        if has_word(word, used_words) or not is_match_word(used_words[-1], word):
            break
        else:
            used_words.append(word)

    game_round = len(used_words)

    people = game_round % n + 1
    order = game_round // n + 1

    if game_round == len(words):
        result = [0, 0]
    else:
        result = [people, order]
    return result


def has_word(word, words):
    if word in words:
        return True
    else:
        return False


def is_match_word(target, current):
    if target[-1] == current[0]:
        return True
    else:
        return False
