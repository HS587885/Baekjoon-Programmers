from collections import deque


def solution(priorities, location):
    q = deque([pri, idx] for idx, pri in enumerate(priorities))
    execution_order = 0
    while q:
        current = q.popleft()
        
        if any(current[0] < item[0] for item in q):
            q.append(current)
        else:
            execution_order +=1
            if current[1] == location:
                return execution_order
