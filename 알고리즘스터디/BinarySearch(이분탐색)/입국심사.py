def solution(n, times):
    left = 1
    right = max(times) * n  # 최악의 경우(가장 느린 심사관이 모든 사람을 처리)

    answer = right

    while left <= right:
        mid = (left + right) // 2
        
        
        total = 0
        for time in times:
            total += mid // time
        
        if total >= n:  
            answer = mid
            right = mid - 1
        else:  
            left = mid + 1

    return answer
