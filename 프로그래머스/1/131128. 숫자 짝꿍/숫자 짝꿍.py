from collections import Counter

def solution(X, Y):
    count_X = Counter(X)
    count_Y = Counter(Y)
    
    result = []
    
    for digit in range(10):
        digit_str = str(digit)
        result += [digit_str] * min(count_X[digit_str], count_Y[digit_str])
    
    if not result:
        return "-1"
    
    if result == ['0'] * len(result):
        return "0"
    
    return "".join(sorted(result, reverse=True))

