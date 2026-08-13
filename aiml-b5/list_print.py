se = set(map(int,input().split()))
sum = 0
for e in se:
    if e%2==0:
        sum+=e
print(sum)