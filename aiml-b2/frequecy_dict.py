li = list(map(int,input().split()))
di = { }
for e in li:
    di[e] = li.count(e)
print(di)