'''Arthamatic operation function'''
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

a = int(input())
b = int(input())
print("Sum = ", add(a,b))
print("sub = ",sub(a,b))
print("mul = ",mul(a,b))
print("div = ",div(a,b))