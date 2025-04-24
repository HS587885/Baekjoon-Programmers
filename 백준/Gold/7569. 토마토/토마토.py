from collections import deque
import sys


def solution(M,N,H):
    arr = []
    q = deque()

    for h in range(H):
        layer = []
        for n in range(N):
            row = list(map(int, sys.stdin.readline().split()))
            for m in range(M):
                if row [m] == 1:
                    q.append((h,n,m,0)) # 층,행,열, 날짜
            layer.append(row)
        arr.append(layer)

    dz = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]

    max_days = 0

    while q:
        z,y,x, days = q.popleft()
        max_days = max(max_days, days)
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nz < H and 0 <= ny <  N and 0 <= nx < M and arr[nz][ny][nx] == 0:
                arr[nz][ny][nx] = 1
                q.append((nz,ny,nx, days + 1))

    for h in range(H):
        for r in range(N):
            for c in range(M):
                if arr[h][r][c] == 0:
                    return -1
    return max_days


M, N, H = map(int, sys.stdin.readline().split())  # 가로, 세로, 높이
print(solution(M, N, H))