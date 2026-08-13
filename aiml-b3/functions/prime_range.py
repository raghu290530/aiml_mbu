def isprime(n):
    if n==1:
        return False
    for i in range(2,n//2 + 1):
        if n%i == 0:
            return False
    return True

#Printing Range of prime nos
n1 = int(input())
n2 = int(input())
for i in range(n1,n2+1):
    if isprime(i):
        print(i,end=" ")
#Printing Prime Factors of ginven no
n3 = int(input())
for i in range(1,n3):
    if n3%i == 0 and isprime(i):
        print(i, end=" ")
