def solution(elements):
    n = len(elements)
    extended_elements = elements * 2
    unique_sums = set()

    for length in range(1, n + 1):  
        for start in range(n):  
            subarray_sum = sum(extended_elements[start:start + length])
            unique_sums.add(subarray_sum)
    
    return len(unique_sums)