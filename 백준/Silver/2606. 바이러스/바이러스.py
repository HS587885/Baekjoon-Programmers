from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())

graph = {i:[] for i in range(1, n+ 1)}
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n + 1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    cnt = 0
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt

print(bfs(1))