from collections import deque
import sys

# 입력 처리
m, n = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()  # 큐 선언
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
                maps[nx][ny] = maps[x][y] + 1  
                q.append((nx, ny))

# BFS 실행
bfs()

# 최소 일수 계산
max_cnt = 0
for row in maps:
    if 0 in row:  
        print(-1)
        exit()
    max_cnt = max(max(row), max_cnt)

print(max_cnt - 1 if max_cnt > 1 else 0)
