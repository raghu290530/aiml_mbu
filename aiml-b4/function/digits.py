'''Write a function digits(n) that calculates
sum of digits, count of digits, reverse of no,
palindrome no, amstrong no
'''

def digit(n):
    t = n
    count = 0
    sum = 0
    rev = 0
    ams = 0
    while t!=0:
        r = t%10
        count += 1
        sum += r
        rev = rev*10 + r
        # ams = ams + r**count
        ams = ams + r**3
        t = t//10
    print("No of digits: ",count)
    print("Sum of digits: ", sum)
    print("Reverse: ",rev)
    if rev==n:
        print("Palindrome")
    else:
        print("Not a palindrome")
    if ams==n:
        print("Amstrong")
    else:
        print("Not Amstrong")

n = int(input())
digit(n)










