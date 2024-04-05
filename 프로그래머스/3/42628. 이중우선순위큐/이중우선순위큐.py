from collections import deque



def solution(operations):
    q = deque()
    for i in operations:
        letter, number_str = i.split()
        number = int(number_str)
        if letter == 'I':
            q.append(number)
        elif letter == 'D' and number > 0 and q:
            max_value = max(q)
            q.remove(max_value)
        elif letter == 'D' and number < 0 and q:
            min_value = min(q)
            q.remove(min_value)

    if not q:
        return [0,0]
    else:
        return [max(q), min(q)]