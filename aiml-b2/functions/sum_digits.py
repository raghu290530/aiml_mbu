from itertools import count
def sum_digits(n):
    t=n
    sum = 0
    count = 0
    rev = 0
    ams = 0
    while t!=0:
        r = t%10
        sum += r
        count += 1
        rev = rev*10 + r
        # ams = ams + r**count
        t //= 10
    print("Sum ", sum)
    print("Cout ", count)
    print("Reverse ", rev)
    if rev == n:
        print("palindrome")
    else:
        print("Not palindrome")
n = int(input())
sum_digits(n)
