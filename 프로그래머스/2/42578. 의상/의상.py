from collections import defaultdict

def solution(clothes):
    category_count = defaultdict(int)
    for _, category in clothes:
        category_count[category] += 1
        
    combinations = 1
    for count in category_count.values():
        combinations *= (count + 1)  
    
    
    return combinations - 1