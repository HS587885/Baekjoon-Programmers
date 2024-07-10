import heapq as hp

def solution(scoville, K):
    hp.heapify(scoville)   
    
    count = 0
    while scoville[0] < K : 
        count += 1
        
        min_one = hp.heappop(scoville)  
        min_two = hp.heappop(scoville)  
        hp.heappush(scoville, min_one + min_two*2)
        
        
        if (len(scoville) == 2) and (scoville[0] + scoville[1]*2) < K: 
            return -1  
        
    return count