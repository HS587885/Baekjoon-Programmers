total_price = int(input())
sum = 0

for _ in range(int(input())):
    a,b = map(int, input().split())
    sum += a * b

print("Yes") if sum == total_price else print("No")