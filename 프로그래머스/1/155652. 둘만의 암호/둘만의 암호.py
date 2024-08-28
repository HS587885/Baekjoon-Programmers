def solution(s, skip, index):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in skip] * 3
    result = ''.join([alphabet[alphabet.index(i) + index] for i in s])
    return result