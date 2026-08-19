from os import fchmod


def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))

def sum_digits(n):
    if n==0:
        return 0
    return n%10 + sum_digits(n//10)
print(sum_digits(156))

def is_prime(n,div=2):
    if n==1:
        return False
    if n==2:
        return True
    if n%div == 0:
        return False
    if div*div > n:
        return True
    return is_prime(n,div+1)

print(is_prime(5))
print()