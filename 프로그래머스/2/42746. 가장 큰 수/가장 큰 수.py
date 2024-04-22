def solution(numbers):
    str_numbers = list(map(str, numbers))
    
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    
    largest_number = ''.join(str_numbers)
    
    if largest_number[0] == '0':
        return '0'
    
    return largest_number