#Write a program to create a tuple of squares from given integers.
n=int(input())
tp = tuple(map(int,input().split()))
li = []
for e in tp:
    li.append(e**2)
print(tuple(li))