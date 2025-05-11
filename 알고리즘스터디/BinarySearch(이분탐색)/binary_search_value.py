# Binary Search Template (2): Searching within a value range
# 최솟값 또는 최댓값을 만족하는 "최적의 값"을 찾는 경우 사용

def binary_search():
    left = 1  # 가능한 최소값 (문제 상황에 따라 설정)
    right = 10**6  # 가능한 최대값 (문제 상황에 따라 설정)
    answer = -1  # 조건을 만족하는 최적의 값을 저장할 변수

    while left <= right:
        mid = (left + right) // 2  # 중간 값 계산

        if condition(mid):  # mid가 조건을 만족하는 경우
            answer = mid  # 현재 mid 저장
            right = mid - 1  # 더 작은 값을 탐색하여 최소값을 찾기
        else:
            left = mid + 1  # mid가 조건을 만족하지 않으면 더 큰 값 탐색

    return answer

# 예시 condition 함수 (문제에 따라 구현 필요)
def condition(x):
    # 예시: x가 특정 조건을 만족하는지 여부
    return True
