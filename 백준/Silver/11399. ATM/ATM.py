n=int(input())
lst=list(map(int,input().split()))
lst.sort()
result=0
time=0
for i in range(n):
    time+=lst[i]
    result+=time
print(result)