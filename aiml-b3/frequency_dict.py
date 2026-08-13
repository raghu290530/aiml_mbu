'''Write a program to count frequency of each element in a list using a dict.
'''
li = list(map(int,input().split()))
di = { }
for e in li:
    if e not in di:
        di[e] = 1
    else:
        di[e] += 1
for x,y in di.items():
    print(x,": ",y)