# def solution(prices):
#     result = []
    
#     for i in range(len(prices)):
#         time_point = prices[i]
#         time = 0
#         for j in range(i + 1, len(prices)):
#             time += 1
#             if time_point > prices[j]:
#                 break
                
#         result.append(time)
    
#     return result

def solution(prices):
    n = len(prices)
    result = [0] * n
    stack = []
    
    for i in range(n):
        # 스택에 있는 인덱스와 현재 주가를 비교하여 주가가 떨어졌다면 스택에서 빼고 시간을 계산
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    
    # 스택에 남아 있는 인덱스에 대해 주가가 끝까지 유지된 경우를 처리
    while stack:
        j = stack.pop()
        result[j] = n - j - 1
    
    return result


            
            