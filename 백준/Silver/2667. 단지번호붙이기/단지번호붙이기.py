import sys
from collections import deque


n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt

answer = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and visited[i][j] == 0:
            result = bfs(i, j)
            answer.append(result)

answer.sort()
print(len(answer))
for num in answer:
    print(num)
