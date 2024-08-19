def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 
             7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    total_days = sum([month[m] for m in range(1, a)]) + b - 1
    
    return day[total_days % 7]


        
        
