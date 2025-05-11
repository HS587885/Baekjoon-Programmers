def solution(id_pw, db):
    answer = ''
    db = [i for i in db if i[0] == id_pw[0]]
    if db == []:
        return "fail"
    else:
        for i in db:
            if i[0] == id_pw[0] and i[1] == id_pw[1]:
                return "login"
            elif (i[0] != id_pw[0] and i[1] == id_pw[1]) or (i[0] == id_pw[0] and i[1] != id_pw[1]):
                return "wrong pw"
            elif i[0] != id_pw[0] and i[1] != id_pw[1]:
                return "fail"
            
    