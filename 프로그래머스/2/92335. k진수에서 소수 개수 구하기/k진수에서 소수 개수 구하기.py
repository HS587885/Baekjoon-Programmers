def iterative(n, base):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return ''.join(str(x) for x in digits[::-1])


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  
    if num % 2 == 0:
        return False  
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    result = iterative(n, k)
    lst =  [i for i in list(result.split('0')) if i.isdigit() == True and is_prime(int(i)) == True]
    return len(lst)

