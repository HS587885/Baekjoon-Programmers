def binary_conversion(s):
    new_s = [i for i in s if i != '0']
    length = len(new_s)
    two_digit = bin(length)[2:]
    cnt = s.count('0')
    return cnt, two_digit

    
def solution(s):
    cnt = 0
    n = 0
    while s != "1":
        n += 1
        cnt_x, s = binary_conversion(s)
        cnt += cnt_x
    return [n, cnt]
