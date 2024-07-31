def solution(hp):
    ants = [5,3,1]
    cnt = 0
    for ant in ants:
        cnt += hp // ant
        hp %= ant 
    return cnt
            