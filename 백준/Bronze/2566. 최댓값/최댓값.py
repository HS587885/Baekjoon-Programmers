T = 9
lst = [list(map(int, input().split())) for _ in range(T)]
maximum  = max([max(i) for i in lst])
print(maximum)
col_lst = [i for i in lst if maximum in i]
col = col_lst[0].index(maximum) + 1
row = lst.index(col_lst[0]) + 1
print(row, col, end=' ')