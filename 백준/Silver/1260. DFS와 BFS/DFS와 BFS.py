def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, v, visited):
    q = [v]
    visited[v] = True
    while q:
        current = q.pop(0)
        print(current, end=" ")
        for neighbor in graph[current]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점의 이웃을 번호 순으로 정렬
for i in range(1, n + 1):
    graph[i].sort()

visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)
