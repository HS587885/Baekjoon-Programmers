def solution(emergency):
    sort = sorted(emergency, reverse = True)
    answer = [sort.index(i) + 1 for i in emergency]
    return answer