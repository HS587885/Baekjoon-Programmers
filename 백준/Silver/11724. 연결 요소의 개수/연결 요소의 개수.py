from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = {i: [] for i in range(1, n+1)}

# 간선 입력
for _ in range(m):  
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

# BFS 함수
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True  
    while q:
        node = q.popleft()
        for neighbor in graph[node]:  
            if not visited[neighbor]: 
                visited[neighbor] = True
                q.append(neighbor)

cnt = 0
for i in range(1, n+1):  # 1부터 n까지 탐색
    if not visited[i]:  # 방문하지 않은 노드가 있다면
        bfs(graph, i, visited)
        cnt += 1

print(cnt) 
