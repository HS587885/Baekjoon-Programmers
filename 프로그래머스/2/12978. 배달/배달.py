import heapq

def solution(N, road, K):
    INF = float('inf')
    graph = [[] for _ in range(N+1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    distance = [INF] * (N+1)
    distance[1] = 0
    
    pq = [(0, 1)]
    
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for neighbor, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    
    return sum(1 for d in distance if d <= K)
