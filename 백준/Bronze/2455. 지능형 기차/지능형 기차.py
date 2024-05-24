lst = [list(map(int, input().split())) for _ in range(4)]

highest = 0
current_num  = 0

for i in range(len(lst)):
    current_num -= lst[i][0]
    #print(current_num)
    current_num += lst[i][1]
    #print(current_num)
    if current_num > highest:
        highest = current_num
        
print(highest)