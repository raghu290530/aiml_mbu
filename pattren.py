n = int(input())
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()
print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
print()
for i in range(n):
    for j in range(n):
        if i==j or i>j:
            print('*',end=' ')
    print()
print()
count = 1
for i in range(n):
    for j in range(1,i+1):
        print(f"{count:3}",end=' ')
        count+=1
    print()
print()
for i in range(n):
    for j in range(i,n):
        print('*',end=' ')
    print()
print()
for i in range(1,n+1):
    for j in range(i,n):
        print('  ',end='')
    for j in range(1,i+1):
        print('*',end=' ')
    print()
print()
for i in range(1,n+1):
    for j in range(i,n):
        print('  ',end='')
    for j in range(1,i+1):
        print('*',end=' ')
    for j in range(1,i):
        print('*',end=' ')
    print()
print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    for j in range((n-i)* 2-1):
        print(' ',end=' ')
    for j in range(1,i+1):
        if j==n:
            continue
        print('*',end=' ')
    print()
print()