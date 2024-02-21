def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    stack_append = stack.append  
    
    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            idx = stack.pop()
            answer[idx] = num
        stack_append(i)  
    return answer
