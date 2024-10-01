from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    result = "".join([i for i in p if p[i] > c[i]])
    return  result
