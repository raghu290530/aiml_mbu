def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    print(f"Factorial of {n} is {f}")
n1 = int(input())
n2 = int(input())
n3 = int(input())
fact(n1)
fact(n2)
fact(n3)