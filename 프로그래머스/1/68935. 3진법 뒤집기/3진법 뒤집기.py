def to_ternary(n):
    ternary = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        ternary = str(remainder) + ternary
    return ternary if ternary else '0'

def solution(n):
    result = to_ternary(n)
    answer = ''.join(list(reversed(result)))
    return int(answer, 3)