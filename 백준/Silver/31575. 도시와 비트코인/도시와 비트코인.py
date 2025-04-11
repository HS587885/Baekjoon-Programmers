from collections import deque
import sys

def solutions(maps,n,m):
    
   
    dx = [1, 0]  
    dy = [0, 1]
    visited = [[False] * m for _ in range(n)]

    def bfs(x,y):
        q = deque([(x,y)])
        while q:
            x, y = q.popleft()
            visited[x][y] = True

            if x == n -1 and y == m - 1:
                return "Yes"
                
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
        return "No"
    return bfs(0,0)
    
m,n = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]      
print(solutions(maps,n,m))
    