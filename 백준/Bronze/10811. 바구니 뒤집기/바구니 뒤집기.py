n,m = map(int, input().split())
bas = [i for i in range(1, n+1)]
temp = 0

for x in range(m):
  i,j = map(int, input().split())
  temp = bas[i-1:j]
  temp.reverse()
  bas[i-1:j] = temp


for x in range(n):
  print(bas[x], end=" ")