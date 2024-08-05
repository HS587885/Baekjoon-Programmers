def solution(common):
    def is_arithmetic(lst):
        difference = lst[1] - lst[0]
        for i in range(1, len(lst) - 1):
            if lst[i + 1] - lst[i] != difference:
                return False
        return True
    
    if is_arithmetic(common) == True:
        return (common[-1] - common[-2]) + common[-1]
    else:
        return (common[-1] // common[-2]) * common[-1]

        
