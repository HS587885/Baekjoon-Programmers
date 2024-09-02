from itertools import combinations
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  
    if n % 2 == 0:
        return False  

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def solution(nums):
    lst = [sum(i) for i in list(combinations(nums, 3))]
    result = [i for i in lst if is_prime(i) == True]   
    return len(result)