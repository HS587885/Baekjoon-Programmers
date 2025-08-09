from collections import deque
import sys



input = sys.stdin.readline

n,m,v = map(int, input().split())

graph = {i: [] for i in range(1,n+1)}

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)


def bfs(start):
    q = deque([start])
    visited[start] = True
    order = []  
    while q:
        node = q.popleft()
        order.append(node)
        for i in sorted(graph[node]):  
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return order

         

visited_dfs = [False] * (n + 1)
def dfs(node):
    visited_dfs[node] = True
    print(node, end=" ")
    for nxt in sorted(graph[node]):
        if not visited_dfs[nxt]:
            dfs(nxt)          
    

dfs(v)
print()
print(*bfs(v))