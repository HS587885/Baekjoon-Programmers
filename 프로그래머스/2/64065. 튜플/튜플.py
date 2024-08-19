from collections import Counter

def solution(s):
    s = list([int(i) for i in s.replace("{", "").replace("}","").split(",")])
    frequency = Counter(s)
    sorted_lst = sorted(s, key=lambda x: (-frequency[x], s.index(x)))
    return list(dict.fromkeys(sorted_lst))
