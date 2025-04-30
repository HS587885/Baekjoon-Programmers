import sys
from collections import deque

n = int(input())  # 컴퓨터 수
m = int(input())  # 연결된 컴퓨터 쌍의 수

# 그래프 초기화 (1번 노드부터 시작)
graph = {i: [] for i in range(1, n + 1)}  

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())  
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)  # 방문 여부 배열

# BFS 함수 정의
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True  
    count = 0  # 감염된 컴퓨터 개수 (1번 제외)

    while q:
        node = q.popleft()
        for neighbor in graph[node]:  
            if not visited[neighbor]:  
                visited[neighbor] = True
                q.append(neighbor)
                count += 1  # 새로 감염된 컴퓨터 수 증가

    return count

# 1번 컴퓨터에서 시작
print(bfs(graph, 1, visited))