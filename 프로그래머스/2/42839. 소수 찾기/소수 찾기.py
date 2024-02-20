from itertools import permutations

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    result = []
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            result.append(int(''.join(j)))


    answer  = [i for i in list(set(result)) if is_prime(i) == True]

    return len(answer)
