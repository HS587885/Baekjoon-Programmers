from collections import deque
import sys

input = sys.stdin.readline


def solution(m,n,k, locations):
    
    maps = [[0] * m for _ in range(n)]


    for loc in locations:
        ly,lx = loc[0],loc[1]
        maps[lx][ly] = 1


    visited = [[0] * m for _ in range(n)]

    def bfs(x,y):
        
        q = deque([(x,y)])
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        visited[x][y] = True
        
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                        maps[nx][ny] = maps[x][y] + 1
                        q.append((nx,ny))
                        visited[nx][ny] = 1
                    
        


    count = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
                count += 1


    return count   
    

T = int(input())
for _ in range(T):
    m,n,k = map(int, input().split())
    locations = [list(map(int, input().split())) for _ in range(k)]
    print(solution(m,n,k, locations))

 