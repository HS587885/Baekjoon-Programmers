def check(lst, a, b):
    result = []
    for i in range(0, len(lst), 2):
        if (lst[i] == a and lst[i + 1] == b) or (lst[i] == b and lst[i + 1] == a):
            return True, result
        if lst[i] == a or lst[i + 1] == a:
            result.append(a)
        elif lst[i] == b or lst[i + 1] == b:
            result.append(b)
        else:
            result.append(lst[i])
    return False, result

def solution(n, a, b):
    lst = list(range(1, n + 1))
    cnt = 0
    while True:
        found, lst = check(lst, a, b)
        cnt += 1
        if found:
            return cnt