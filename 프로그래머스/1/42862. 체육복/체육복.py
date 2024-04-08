def solution(n, lost, reserve):
    reserve_d = set(reserve) - set(lost)
    
    lost_d = set(lost) - set(reserve)
    
    for i in reserve_d:
        if (i - 1) in lost_d:
            lost_d.remove(i - 1)
        elif (i + 1) in lost_d:
            lost_d.remove(i + 1)
            
    return n - len(lost_d)