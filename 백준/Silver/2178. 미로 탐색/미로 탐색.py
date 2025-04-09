from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

def solutions(maps):
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y):
        q = deque([(x,y)])
        
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx,ny))
        return maps[n-1][m-1]
    return bfs(0,0)

print(solutions(maps))