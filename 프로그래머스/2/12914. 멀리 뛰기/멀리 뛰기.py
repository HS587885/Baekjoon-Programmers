def solution(n):
    lst = [0] * (n + 1)
    lst[0] = 1 
    if n >= 1:
        lst[1] = 1 
    if n >= 2:
        lst[2] = 2  
    
    for i in range(3, n + 1):
        lst[i] = lst[i - 1] + lst[i - 2]
    
    return lst[n] % 1234567