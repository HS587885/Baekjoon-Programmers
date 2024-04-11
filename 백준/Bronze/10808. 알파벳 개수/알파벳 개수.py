S = input()

word_lst = list(S)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = {i:0 for  i in alphabet}
for i in word_lst:
    answer[i] += 1

for z in answer.values():
    print(z)