from collections import deque

def galho(s):
    de = deque(s)
    temp = []
    start = ['[', '(', '{']
    end = [']', ')', '}']
    
    while de:
        tp = de.popleft()
        if tp in start:
            temp.append(tp)
        else:
            if not temp:
                return False
            top = temp.pop()
            if (top == '[' and tp != ']') or (top == '(' and tp != ')') or (top == '{' and tp != '}'):
                return False
    return not temp  # 스택이 비어 있으면 True, 그렇지 않으면 False

def solution(s):
    original = deque(s)
    ds = deque(s)
    cnt = 0
    
    for _ in range(len(s)):
        if galho(ds):
            cnt += 1
        ds.append(ds.popleft())  # 문자열을 회전
        if ds == original:
            break
            
    return cnt