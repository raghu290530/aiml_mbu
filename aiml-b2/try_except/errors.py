# x = int(input()) ValueError
# x = 5/0  ZeroDivisionError
# x = y+5  NameError
# li = [5,6,9]
# print(li[3]) IndexError
try:
    x=int(input())
    y = int(input())
    print(x/y)
    li = [5]
    print(li[2])
except ValueError:
    print("Enter Integer only")
except ZeroDivisionError:
    print("y should not be zero")
except:
    print("Something went wrong")
else:
    print("Nothing wrong")