n = int(input())
di = { }
for i in range(n):
    li = input().split()
    di[li[0]] = int(li[1])
print(di)
m = max(di.values())
print(m)
for k in di:
    if di[k] == m:
        print(k)
        break