#Binary Search Template (1): Searching within index range

def binary_search(target, arr):
    left = 0  # 시작 인덱스
    right = len(arr) - 1  # 끝 인덱스

    while left <= right:
        mid = (left + right) // 2  # 중간 인덱스 계산

        if arr[mid] == target:
            return mid  # 값을 찾은 경우 해당 인덱스 반환
        elif arr[mid] < target:
            left = mid + 1  # 오른쪽 절반 탐색
        else:
            right = mid - 1  # 왼쪽 절반 탐색

    return -1  # 값을 찾지 못한 경우 -1 반환
