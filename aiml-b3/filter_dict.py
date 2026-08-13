n = int(input())
di = { }
for i in range(n):
    li = input().split()
    di[li[0]] = int(li[1])
T = int(input())
new_di = { }
for k in di:
    if di[k] > T:
        new_di[k] = di[k]
print(new_di)