from itertools import combinations
from collections import deque
import copy
import sys

n, m  = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def solutions(maps, n,m):
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    empty_spaces = []  # 빈 공간 (벽을 세울 수 있는 후보)
    viruses = []  # 바이러스 위치
    
    # 빈 칸과 바이러스 위치 저장
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                empty_spaces.append((i, j))
            elif maps[i][j] == 2:
                viruses.append((i, j))
    
    def bfs(lab):
        queue = deque(viruses)  # 초기 바이러스 위치에서 시작
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
                    lab[nx][ny] = 2  # 바이러스 전파
                    queue.append((nx, ny))
    
    max_safe_area = 0
    
    # 벽을 세울 수 있는 모든 조합 탐색
    for walls in combinations(empty_spaces, 3):
        # 원본 연구소 배열을 복사 (deepcopy)
        lab_copy = copy.deepcopy(maps)
        
        # 벽 세우기
        for x, y in walls:
            lab_copy[x][y] = 1
        
        # 바이러스 전파 실행
        bfs(lab_copy)
        
        # 안전 영역 계산 (0의 개수)
        safe_area = sum(row.count(0) for row in lab_copy)
        max_safe_area = max(max_safe_area, safe_area)
    
    return max_safe_area

print(solutions(maps, n,m))  
