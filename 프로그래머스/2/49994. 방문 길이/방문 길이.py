def solution(dirs):
    commands = list(dirs)
    start_point = [0, 0]
    visited = set()
    cnt = 0
    
    for i in commands:
        next_point = start_point.copy()
        
        if i == "R":
            next_point[0] += 1
        elif i == "L":
            next_point[0] -= 1
        elif i == "U":
            next_point[1] += 1
        elif i == "D":
            next_point[1] -= 1
        
        if -5 <= next_point[0] <= 5 and -5 <= next_point[1] <= 5:
            path = (start_point[0], start_point[1], next_point[0], next_point[1])
            reverse_path = (next_point[0], next_point[1], start_point[0], start_point[1])
            if path not in visited and reverse_path not in visited:
                visited.add(path)
                cnt += 1
            start_point = next_point
            
    return cnt
