def solution(babbling):
    lst = ["aya", "ye", "woo", "ma"]
    

    for i in range(len(babbling)):
        for j in lst:
            babbling[i] = babbling[i].replace(j, "0")
    return len([s for s in babbling if set(s) == {"0"}])