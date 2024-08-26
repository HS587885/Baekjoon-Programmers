import re

def check(word):
    pro = ["aya", "ye", "woo", "ma"]
    for j in pro:
        if j in word:
            word = word.replace(j, " ")#strip(j)
    return word

def solution(babbling):
    double =  ["ayaaya", "yeye", "woowoo", "mama"]

    b = [string for string in babbling if not any(pattern in string for pattern in double)]
    result = [check(b[i]) for i in range(len(b)) if bool(re.search(r'[a-zA-Z]', check(b[i]))) == False]
    return  len(result)#.count(" ")