# import numpy as np

# def solution(arr1, arr2):
#     arr1 = np.array(arr1)
#     arr2 = np.array(arr2)
#     result = arr1 + arr2
#     return result.tolist() 


def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)
    return answer
