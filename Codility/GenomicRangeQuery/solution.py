# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    result = []
    for i in range(len(P)):
        dna = S[P[i]:Q[i] + 1]
        if 'A' in dna:
            num = 1
        elif 'C' in dna:
            num = 2
        elif 'G' in dna:
            num = 3
        elif 'T' in dna:
            num = 4
        result.append(num)
    return result
