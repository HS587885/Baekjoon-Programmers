
# 소수 판별
def primenumber(x):
    import math
    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0:		
        	return False
    return True		

def solution(n):
    answer = [z for z in range(2, n+1) if primenumber(z) == True]
    return len(answer)