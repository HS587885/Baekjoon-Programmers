students = [i for i in range(1,31)]

for _ in range(28):
    lst = int(input())
    students.remove(lst) 

print(min(students))
print(max(students))