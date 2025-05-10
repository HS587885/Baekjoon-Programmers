def solution(order):
    answer = 0
    num = str(order)
    for j in ['3','6','9']:
        answer += num.count(j)
    return answer