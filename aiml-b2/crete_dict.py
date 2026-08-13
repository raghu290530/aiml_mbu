n = int(input())
key = tuple(input().split())
values = tuple(input().split())
di = {}
for i in range(n):
    di[key[i]]=values[i]
print(di)
