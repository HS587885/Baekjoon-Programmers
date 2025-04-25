import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().split())  # 정점, 간선 수
K = int(input())  # 시작 정점

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

# 간선 정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라 알고리즘
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for neighbor, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

dijkstra(K)

# 결과 출력
for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])