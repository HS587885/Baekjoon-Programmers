# def solution(num, total):
#     if num == 3 or total % num != 0 :
#         guideline = total // num -1
#         return [i for i in range(guideline, guideline + num)]
#     else:
#         guideline = total // num -2
#         return [i for i in range(guideline, guideline + num)]
    
        
def solution(num, total):
    central_value = total // num
    
    start_value = central_value - (num - 1) // 2
    
    return [start_value + i for i in range(num)]
