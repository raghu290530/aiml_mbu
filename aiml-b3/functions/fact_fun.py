'''Function with arguments and without return'''
def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    print(f"Factorial of {n} is {f}")
fact(5)
