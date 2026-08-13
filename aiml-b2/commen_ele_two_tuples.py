''' find the common ele in two tuples'''
tp1 = tuple(map(int,input().split()))
tp2 = tuple(map(int,input().split()))
li = []
for e in tp1:
    if e in tp2:
        li.append(e)
print(tuple(li))