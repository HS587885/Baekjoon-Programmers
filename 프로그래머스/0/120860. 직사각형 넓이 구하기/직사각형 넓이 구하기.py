def solution(dots):
    answer = 0
    x = [i[0] for i in dots]
    y = [i[1] for i in dots]
    width = max(x) - min(x)
    height = max(y) - min(y)
    return width * height