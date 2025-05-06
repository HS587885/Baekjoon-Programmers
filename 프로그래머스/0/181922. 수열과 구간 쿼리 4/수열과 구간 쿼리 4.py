def solution(arr, queries):
    for num in range(len(queries)):
        s,e,k = queries[num][0], queries[num][1], queries[num][2]
        for i in range(s,e+1):
            if i % k == 0:
                arr[i] += 1
            
        
    return arr