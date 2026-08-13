def greet(name):
    print(f"Hello {name}!")
# in_name = input()
# greet(in_name)
greet(5)
greet([5,9,6,8])
#function can accept any data type

def square(n):
    return n*n
print(square(9))

def print_numbers(n):
    for i in range(1,n+1):
        print(i)
print_numbers(5)