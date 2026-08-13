#Write a program to find the second largest element in a list of distinct integers.
from enum import unique

n = int(input())
li = list(map(int,input().split()))
print(li)
uli = []
for e in li:
    if e not in uli:
        uli.append(e)
print(uli)
uli.sort()
print(uli[-2])