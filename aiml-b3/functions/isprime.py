def isprime(n):
    if n==1 or n==0:
        return False
    for i in range(2,n//2 + 1):
        if n%i == 0:
            return False
    return True
if isprime(50):
    print("Prime")
else:
    print("Not Prime")