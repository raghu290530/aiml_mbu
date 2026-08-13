'''5 -> 5*4*3*2*1 ->120'''
n1 = int(input())
n2 = int(input())
n3 = int(input())
f1 = 1
for i in range(1,n1+1):
    f1 *= i
print(f"Factorial of {n1} is {f1}")
f2 = 1
for i in range(1,n2+1):
    f2 *= i
print(f"Factorial of {n2} is {f2}")
f3 = 1
for i in range(1,n3+1):
    f3 *= i
print(f"Factorial of {n3} is {f3}")