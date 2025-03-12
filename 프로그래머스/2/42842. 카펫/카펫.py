import math
def solution(brown, yellow):
    total = brown + yellow
    num = math.sqrt(total)
    if num.is_integer() == True:
        return [num, num]
    else:
        diff = total
        lst = [i for i in range(1,total+1) if total % i == 0]
        for i in lst:
            ob = total // i
            if i >= ob and i * ob == total:
                return [i, ob]
            if (i - 2) * (ob - 2) == yellow:
                return [ob, i]
                  