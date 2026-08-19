try:
    a = int(input())
    b = int(input())
    print(a/b)
except ValueError:
    print("Enter integers only")
except ZeroDivisionError:
    print("B should not be Zero")
