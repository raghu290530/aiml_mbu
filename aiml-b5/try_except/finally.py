'''Write a program that tries to convert
to int and always prints 'Done' in finally.
'''
try:
    a = int(input())
    print(a)
except:
    print("Integer only")
finally:
    print("Done")