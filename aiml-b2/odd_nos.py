'''W.A.P to print all odd nos between a range'''
n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    if i%2==1:
        print(i,end=" ")