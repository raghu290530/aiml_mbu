'''Write a function digits(n), count of digits,
reverse no, amstrong no, palinrome number,'''
from itertools import count


def digits(n):
    t = n
    count=0
    sum = 0
    rev = 0
    ams = 0
    while t!=0:
        r = t%10  #reminder
        count +=1
        sum += r
        rev = rev*10 + r
        # ams = ams + r**count
        ams = ams + r**3
        t = t//10
    print("Count =", count)
    print("Sum =",sum)
    print("Reverse = ",rev)
    if rev == n:
        print("Palindome")
    else:
        print("Not palindrome")
    if ams == n:
        print("Amstrong")
    else:
        print("Not Amstrong")

n = int(input())
digits(n)