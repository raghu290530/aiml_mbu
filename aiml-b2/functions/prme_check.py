'''Write a function is_prime(n) that returns True if n is prime, else False.'''
def is_prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
    return True
#Range of prime numbers
n1 = int(input())
n2 = int(input())
for i in range(n1,n2):
    if is_prime(i):
        print(i)
#Print all prime factors of a given number
n = 28
for i in range(2,n):
    if n%i == 0 and is_prime(i):
        print(i,end=" ")
