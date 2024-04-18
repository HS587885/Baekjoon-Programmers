def solution(strings, n):
    sorted_list = sorted(strings, key=lambda x: (x[n], x))
    return sorted_list