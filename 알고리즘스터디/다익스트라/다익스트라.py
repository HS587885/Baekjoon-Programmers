import heapq
import sys

sys.stdin = open('/Users/hyunghoon/Desktop/머신러닝연습/알고리즘공부/input.txt', 'rt')


n,m = map(int, sys.stdin.readline().split())

graph = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

def dijkstra(n, graph):
    INF = float('inf')
    distance = [INF] * (n+1)
    distance[1] = 0

    pq = [(0,1)]
    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue
        
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]: 
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
    return distance[n]

print(dijkstra(n, graph))