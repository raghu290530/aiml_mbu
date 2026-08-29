'''Write a program that composes two functions: f(x) = x + 1 and g(x) = x * 2.
Read x and print f(g(x)) and g(f(x)) on separate lines.'''

def f(x):
    return x+1
def g(x):
    return x*2

print(f(g(5)))
print(g(f(5)))