def solution(s):
    if len(s) % 2 == 0:
        st = len(s) // 2
        return s[st-1:st+1]
    else:
        st = len(s) // 2
        return s[st]