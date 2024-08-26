def solution(q, r, code):
    result = [code[i] for i in range(len(code)) if i % q == r]
    return ''.join(result) if result != [] else ''.join(code)