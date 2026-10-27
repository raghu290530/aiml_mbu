'''Write a program that tries
to convert to int and always prints
'Done' in finally.
'''
try:
    x = int(input())
    print(x)
except:
    print("Invalid number")
finally:
    print("Done")