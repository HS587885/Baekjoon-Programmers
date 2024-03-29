T = 5
lst = [list(map(str,input())) for _ in range(T)]



def vertical(lst,j):
    word = []
    for i in range(len(lst)):
        try:
            word.append(lst[i][j])
        except:
            pass 
    return word


large = max([len(i) for i in lst])
answer = []
for i in range(large):
    answer.append(vertical(lst,i))

result = sum(answer, [])
print(''.join(result))