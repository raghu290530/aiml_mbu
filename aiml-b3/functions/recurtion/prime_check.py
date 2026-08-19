def is_prime(n,i):
    if n==1:
        return False
    if n==2:
        return True
    if i >n//2 +1:
        return True
    if n%i == 0:
        return False
    return is_prime(n,i+1)
print(is_prime(3,2))