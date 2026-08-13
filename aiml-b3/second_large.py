n = int(input())
li = list(map(int,input().split()))
max = max(li)

while max in li:
    li.remove(max)
li.sort()
print(li[-1])