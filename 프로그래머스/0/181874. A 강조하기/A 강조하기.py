def solution(myString):
    return ''.join('A' if i in 'aA' else i.lower() for i in myString)
