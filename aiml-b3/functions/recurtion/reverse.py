def reverse(n,rev):
    if n==0:
        return 0
    return reverse(n,n//10 +n%10)

print(reverse(123,0))