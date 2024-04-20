def solution(want, number, discount):
    if want[0] not in discount:
        return 0
    else:
        cnt = 0
        lst = sorted([item for item, count in zip(want, number) for _ in range(count)])
        for i in range(len(discount)):
            dist_memo = sorted(discount[i:i+10])
            if lst == dist_memo:
                cnt += 1
            
        return cnt

            
    
