from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    #graph = {i: [j for j in range(n) if computers[i][j] == 1 and i != j] for i in range(n)}
    graph = {i: [j for j in range(n) if computers[i][j] == 1] for i in range(n)}

    
    def bfs(start):
        q = deque([start])
        visited[start] = True
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

    for i in range(n):
        if not visited[i]: 
            bfs(i)
            answer += 1  

    return answer
