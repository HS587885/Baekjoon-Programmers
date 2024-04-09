from collections import deque


def bfs(n,computers, node, visited):
    que = deque()
    visited[node] = True
    que.append(node)
    while que:
        node = que.popleft()
        visited[node] = True
        for next_node in range(n):
            if next_node != node and computers[node][next_node] == 1:
                if visited[next_node] == False:
                    que.append(next_node)
                
def solution(n, computers):
    visited = [False for _ in range(n)]
    count = 0
    for node in range(n):
        if visited[node] == False:
            bfs(n, computers, node, visited)
            count += 1
    return count