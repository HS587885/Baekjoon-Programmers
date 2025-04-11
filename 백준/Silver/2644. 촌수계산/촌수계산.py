from collections import deque

# 입력 받기
n = int(input())  # 전체 사람 수
a, b = map(int, input().split())  # 촌수를 계산해야 하는 두 사람
m = int(input())  # 부모 자식 관계 개수

# 그래프 초기화
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# BFS를 이용한 최단 거리 탐색
def bfs(start, target):
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    
    while queue:
        node, depth = queue.popleft()
        if node == target:
            return depth
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))
    
    return -1

# 결과 출력
print(bfs(a, b))
