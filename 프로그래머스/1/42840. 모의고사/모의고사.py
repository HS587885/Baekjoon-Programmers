def solution(answers):
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    pattern1 = a1 * ((len(answers) // len(a1)) + 1)
    pattern2 = a2 * ((len(answers) // len(a2)) + 1)
    pattern3 = a3 * ((len(answers) // len(a3)) + 1)
    
    counts = [sum(ans == a for ans, a in zip(answers, pattern)) for pattern in (pattern1, pattern2, pattern3)]
    
    max_count = max(counts)
    
    answer = [i + 1 for i, count in enumerate(counts) if count == max_count]
    
    return answer
