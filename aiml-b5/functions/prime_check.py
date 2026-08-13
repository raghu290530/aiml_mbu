'''Write a function is_prime(n) that returns True if n is prime, else False.'''
def is_prime(n):
    if n<0:
        return
    if n==0 or n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
print(is_prime(5))
print(is_prime(50))
print(is_prime(97))
print(is_prime(0))
print(is_prime(-1))