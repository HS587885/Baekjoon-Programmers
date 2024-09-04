def solution(sequence, k):
    start = 0
    current_sum = 0
    min_length = float('inf')
    answer = []

    for end in range(len(sequence)):
        current_sum += sequence[end]

        while current_sum > k and start <= end:
            current_sum -= sequence[start]
            start += 1

        if current_sum == k:
            if end - start < min_length:
                min_length = end - start
                answer = [start, end]

    return answer if answer else []
