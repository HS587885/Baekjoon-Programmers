def solution(array, commands):
    answer = []
    for command in commands:
        start, end, position = command
        sorted_subarray = sorted(array[start-1:end])
        answer.append(sorted_subarray[position-1])
    return answer
