def solution(left, right):
    lst = [i for i in range(left, right+1)]
    check = []
    cnt = 0
    for i in lst:
        factor = []
        for j in range(1,i+1):
            if i % j == 0:
                factor.append(j)
        if len(factor) % 2 == 0:
            cnt += i
        else:
            cnt -= i

    return cnt