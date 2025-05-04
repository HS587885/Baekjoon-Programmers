def solution(park, routes):
    maps = []
    start = (0,0)
    for i in range(len(park)):
        temp = []
        track = park[i]
        for j in range(len(track)):
            if track[j] == "S":
                start = (i,j)
                temp.append(0)
            
            elif track[j] == "O":
                temp.append(0)
            
            else:
                temp.append(1)
        maps.append(temp)
        
    n = len(park)
    m = len(park[0])
    
    direction = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)}
    
    x, y = start
    
    for command in routes:
        op, num = command.split()
        num = int(num)
        dx ,dy = direction[op]
        
        success = True
        
        for step in range(1, num + 1):
            tx = x + dx * step
            ty = y + dy * step
            if not (0 <= tx < n and 0 <= ty < m) or maps[tx][ty] == 1:
                success = False
                break
        
        if success:
            x += dx * num
            y += dy * num
            
    return [x,y]
        