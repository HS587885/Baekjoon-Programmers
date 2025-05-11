def solution(spell, dic):
    check = sorted(spell)
    new_dic = [i for i in dic if check == sorted(list(i))]
    return 2 if new_dic == [] else 1