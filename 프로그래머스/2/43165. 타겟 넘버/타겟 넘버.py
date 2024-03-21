from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    q = deque()
    q.append((0,0))
    
    while q:
        x, y = q.popleft()
        if y == n:
            if x == target:
                answer += 1
        else:
            number = numbers[y]
            q.append((x + number, y+ 1))
            q.append((x - number, y+ 1))
            
    return answer
                
