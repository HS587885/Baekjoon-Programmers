def length_maker(lst, n):
    for i in range(len(lst)):
        check = len(lst[i]) 
        if check < n:
            plus_factor = '0' * (n - check)
            lst[i] = plus_factor + lst[i]
    return lst

def solution(n, arr1, arr2):
    answer = []
    arr_one = [bin(i)[2:] for i in arr1]
    arr_one = length_maker(arr_one,n)
    arr_two = [bin(i)[2:] for i in arr2]
    arr_two = length_maker(arr_two,n)
    
    answer = []
    for i in range(n):
        row = ''
        for j in range(n):
            if arr_one[i][j] == '1' or arr_two[i][j] == '1':
                row += '#'
            else:
                row += ' '
        answer.append(row)

    return answer