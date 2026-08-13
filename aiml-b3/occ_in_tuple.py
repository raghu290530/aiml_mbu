n = int(input())
tp = tuple(map(int,input().split()))
li = []
for e in tp:
    if e not in li:
        li.append(e)
for e in li:
    print(e,"-",tp.count(e))