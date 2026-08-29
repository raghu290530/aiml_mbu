def min_max(lst):
    return [min(lst),max(lst)]

li = list(map(int,input().split()))
mimx = min_max(li)
print(mimx[0],mimx[1])