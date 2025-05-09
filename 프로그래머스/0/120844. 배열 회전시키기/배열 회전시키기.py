from collections import deque

def solution(numbers, direction):
    q = deque(numbers)
    switch = True
    while switch:
        if direction == "right":
            go_left = q.pop()
            q.appendleft(go_left)
            switch = False
            return list(q)
        else:
            go_right = q.popleft()
            q.append(go_right)
            switch = False
            return list(q)
            
        
    
   