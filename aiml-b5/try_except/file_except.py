'''Write a program that tries to open
'missing.txt' and catches FileNotFoundError.
'''
try:
    f = open("missing1.txt",'r')
    print("File Opened")
except FileNotFoundError:
    print("File Not found")