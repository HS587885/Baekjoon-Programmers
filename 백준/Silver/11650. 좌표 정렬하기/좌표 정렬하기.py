n = int(input())
array = []

for i in range(n):
    a, b = map(int, input().split())
    array.append([a,b])
array.sort()

for a, b in array:
    print(a, b) 