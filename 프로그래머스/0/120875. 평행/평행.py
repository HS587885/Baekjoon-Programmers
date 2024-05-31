def slope(dot1, dot2):
    if dot1[0] == dot2[0]:  
        return float('inf')
    return (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])

def solution(dots):
    if slope(dots[0], dots[1]) == slope(dots[2], dots[3]):
        return 1
    if slope(dots[0], dots[2]) == slope(dots[1], dots[3]):
        return 1
    if slope(dots[0], dots[3]) == slope(dots[1], dots[2]):
        return 1
    return 0