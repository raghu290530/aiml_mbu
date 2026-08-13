n = int(input())
k = list(map(str,input().split()))
v = list(map(int,input().split()))
di = { }
# se = set()
for i in range(n):
    di[k[i]] = v[i]
print(di)