# def tired_score(lst):
#     result = [i ** 2 for i in lst]
#     return sum(result)
    

# def solution(n, works):
#     sorted_work = sorted(works, reverse=True)
#     if n == 1:
#         sorted_work[0] -= 1
#         return tired_score(sorted_work)
#     if len(works) < n and sum(works) < n:
#         return 0
    
#     while n > 0:
#         sorted_work[0] -= 1
#         sorted_work = sorted(sorted_work, reverse=True)
#         #print(sorted_work)
#         n -= 1
#     return tired_score(sorted_work)

import heapq

def tired_score(lst):
    result = sum(i ** 2 for i in lst)
    return result

def solution(n, works):
    if sum(works) <= n:
        return 0

    max_heap = [-work for work in works]
    heapq.heapify(max_heap)

    while n > 0:
        max_work = heapq.heappop(max_heap)
        if max_work == 0:
            break
        max_work += 1
        heapq.heappush(max_heap, max_work)
        n -= 1

    return tired_score(max_heap)