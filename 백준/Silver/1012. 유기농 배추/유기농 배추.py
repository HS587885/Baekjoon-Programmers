from collections import deque
import sys

def solution(maps, m, n):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[False] * m for _ in range(n)]

    
    def bfs(x,y):
        q = deque([(x,y)])
        visited[x][y] = True
        cnt = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
                    cnt += 1
        return cnt
        
    max_cnt = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and not visited[i][j]:
                max_cnt.append(bfs(i,j))
    return len(max_cnt)



T = int(sys.stdin.readline())

for _ in range(T):
    m,n,k = map(int, sys.stdin.readline().split())
    cabbage_location  = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
    
    maps = [[0 for _ in range(m)] for _ in range(n)]
    for i in cabbage_location:
        maps[i[1]][i[0]] = 1

    print(solution(maps, m, n))