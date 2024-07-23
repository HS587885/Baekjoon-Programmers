from collections import deque

def solution(x, y, n):
    if x == y:
        return 0

    visited = set()  
    queue = deque([(x, 0)])  

    while queue:
        current, count = queue.popleft()

        if current == y:  
            return count

        
        for operation in [current + n, current * 2, current * 3]:
            if operation not in visited and operation <= y:  
                visited.add(operation)
                queue.append((operation, count + 1))

    return -1 