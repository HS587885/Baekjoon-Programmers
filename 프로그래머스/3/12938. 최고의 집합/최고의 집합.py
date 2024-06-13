def solution(n, s):
    if s < n:
        return [-1]
    
    quotient, remainder = divmod(s, n)
    
    # 정수 조합 생성
    result = [quotient] * n
    for i in range(remainder):
        result[i] += 1
    
    return sorted(result)