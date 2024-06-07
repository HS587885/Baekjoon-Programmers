def solution(arr):
    min_val = min(arr)
    result = []
    for i in arr:
        if i != min_val:
            result.append(i)
    return result if result else [-1]
