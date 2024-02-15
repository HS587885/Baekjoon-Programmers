def solution(people, limit):
    people = sorted(people)
    
    start, end = 0, len(people)-1

    
    cnt = 0

    while start <= end:
        cnt += 1
        if (people[start] + people[end] <= limit):
            start += 1
            end -= 1
        else:
            end -= 1

    return cnt  
            
            
            
            

            
       
            
       
                
                
            
  
            
        
            
        
        
            
   