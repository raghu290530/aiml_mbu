n = int(input())
r = int(input())
def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return  f
ncr = fact(n)/(fact(r)*fact(n-r))
print("nCr = ", int(ncr))
