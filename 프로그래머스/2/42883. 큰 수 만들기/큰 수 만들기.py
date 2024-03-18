def solution(number, k):
    stack = []

    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    while k > 0:
        stack.pop()
        k -= 1

    answer = ''.join(stack)
    return answer
