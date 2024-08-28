def solution(prices):
    result = []
    
    for i in range(len(prices)):
        time_point = prices[i]
        time = 0
        
        for j in range(i + 1, len(prices)):
            time += 1
            if time_point > prices[j]:
                break
                
        result.append(time)
    
    return result

            
            