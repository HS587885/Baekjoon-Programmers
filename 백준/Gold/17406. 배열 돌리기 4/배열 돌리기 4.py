import sys
import copy
from itertools import permutations

def rotate(arr, op):
    r, c, s = op
    r -= 1
    c -= 1
    new_arr = copy.deepcopy(arr)

    for layer in range(1, s + 1):
        top = r - layer
        left = c - layer
        bottom = r + layer
        right = c + layer

        # top row
        for i in range(left + 1, right + 1):
            new_arr[top][i] = arr[top][i - 1]
        # right column
        for i in range(top + 1, bottom + 1):
            new_arr[i][right] = arr[i - 1][right]
        # bottom row
        for i in range(right - 1, left - 1, -1):
            new_arr[bottom][i] = arr[bottom][i + 1]
        # left column
        for i in range(bottom - 1, top - 1, -1):
            new_arr[i][left] = arr[i + 1][left]

    return new_arr

def get_min_row_sum(arr):
    return min([sum(row) for row in arr])

# 입력
N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
rotations = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]

# 가능한 모든 연산 순서에 대해 최소값 갱신
answer = float('inf')
for order in permutations(rotations, K):
    temp = copy.deepcopy(A)
    for op in order:
        temp = rotate(temp, op)
    answer = min(answer, get_min_row_sum(temp))

print(answer)
