def solution(clothes):
    clothes_dict = {}
    
   
    for item, type in clothes:
        if type not in clothes_dict:
            clothes_dict[type] = 2  
        else:
            clothes_dict[type] += 1
    
    
    answer = 1
    for key in clothes_dict:
        answer *= clothes_dict[key]
    
    return answer - 1