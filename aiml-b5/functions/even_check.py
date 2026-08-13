'''Write a function is_even(n) that returns True if n is even, else False.
'''

def is_even(n):
    if n%2==0:
        return True
    return False
print(is_even(6))
print(is_even(5))

def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b
print(max_of_two(4,9))
print(max_of_two(3,2))
print(max_of_two(5,5))