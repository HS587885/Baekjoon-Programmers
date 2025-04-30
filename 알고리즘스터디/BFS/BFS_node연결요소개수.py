import sys
from collections import deque
#sys.stdin = open('/Users/hyunghoon/Desktop/머신러닝연습/electricCar/input.txt', 'rt')

n, m = map(int, sys.stdin.readline().split())

# 그래프 초기화 (1번 노드부터 시작)
graph = {i: [] for i in range(1, n + 1)}  

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())  
    graph[a].append(b)
    graph[b].append(a)

answer = 0  
visited = [False] * (n + 1)  # ✅ 1번부터 사용

# BFS 함수 정의
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True  
    while q:
        node = q.popleft()
        for neighbor in graph[node]:  
            if not visited[neighbor]:  
                visited[neighbor] = True
                q.append(neighbor)

# 연결 요소 개수 세기
for i in range(1, n + 1):  
    if not visited[i]:  
        bfs(graph, i, visited)  
        answer += 1  

print(answer)