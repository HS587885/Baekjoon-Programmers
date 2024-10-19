def solution(phone_number):
    end = phone_number[-4:]
    start = phone_number[:-4]
    answer = '*' * len(start)
    return answer + end