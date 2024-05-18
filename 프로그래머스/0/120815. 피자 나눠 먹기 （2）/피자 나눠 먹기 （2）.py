from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def solution(n):
    if n % 6 == 0:
        return n / 6
    else:
        result = lcm(n, 6)
        return result / 6
        