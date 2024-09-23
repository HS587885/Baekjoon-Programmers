from itertools import combinations

def solution(number):
    lst = [i for i in list(combinations(number, 3)) if sum(i) == 0]
    return len(lst)