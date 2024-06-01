A = input()
B = input().split()

result = list(A)
for i in range(len(result)):
    if result[i] in B:
        result[i] = result[i].lower()

print(''.join(result))
