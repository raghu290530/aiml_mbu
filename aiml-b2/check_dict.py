''' Write a program to get the value for a given key. If key missing, print "Key not found".'''
''' 
3
a 1
b 2
c 3
b
'''
n = int(input())
di = {}
for i in range(n):
    li = input().split()
    di[li[0]]=li[1]
print(di)
key = input()
if key in di:
    print(di[key])
else:
    print("Not found")