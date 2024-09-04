def solution(s, n):
    lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]  
    upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  
    answer = []
    
    for char in s:
        if char.isupper():
            idx = (upper.index(char) + n) % len(upper)
            answer.append(upper[idx])
        elif char.islower():
            idx = (lower.index(char) + n) % len(lower)
            answer.append(lower[idx])
        else:
            answer.append(char)
    
    return ''.join(answer)  


