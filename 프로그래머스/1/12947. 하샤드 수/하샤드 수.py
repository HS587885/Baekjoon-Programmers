def solution(x):
    answer = True
    total = sum([int(i) for i in list(str(x))])
    if x % int(total) == 0:
        answer = True
    else:
        answer = False
    return answer