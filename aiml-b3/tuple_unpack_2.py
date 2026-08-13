n=int(input())
tp = tuple(map(int,input().split()))
a,*b,c = tp
if a+c == sum(b):
    print("Xylem")
else:
    print("Phloem")