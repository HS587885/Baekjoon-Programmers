import sys
from collections import deque


m, n = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

maps = [[1 if j == '*' else 0 for j  in i ] for i in graph]

def solutions(maps,m ,n):

    visited = [[False] * m for _ in range(n)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def bfs(x,y):
        q = deque([(x,y)])
        visited[x][y] = True
        cnt = 1

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    cnt += 1
        return cnt

    max_cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and not visited[i][j]:
                max_cnt = max(max_cnt, bfs(i,j))
    return max_cnt

print(solutions(maps, m, n))               

