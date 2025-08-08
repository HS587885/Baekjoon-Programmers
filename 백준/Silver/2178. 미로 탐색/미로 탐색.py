from collections import deque
import sys


n,m = map(int, sys.stdin.readline().split())
#print(n,m)
maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]


def bfs(x,y):
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
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

print(bfs(0,0))