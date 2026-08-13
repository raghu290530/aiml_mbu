'''fibonacci'''
'''Write a function fibonacci(n) that returns the nth Fibonacci number (0-indexed).'''
def fibonacci(n):
    if n==0 or n==1:
        return 0
    a,b = 0,1
    for i in range(1,n):
        c = a+b
        a,b = b,c
    return b
n = int(input())
print(fibonacci(n))
