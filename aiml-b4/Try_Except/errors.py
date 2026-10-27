# print(x)  NameError:
# x = int(input()) ValueError:
# y = 20 /0 ZeroDivisionError:
# li = [5,6,9]
# print(li[3]) IndexError:
try:
    a = int(input())
    b = int(input())
    c = a/b
    print(c)
    li = [5,6,9]
    print(li[3])
    print(d)
except ValueError:
    print("Enter Integer Only")
except ZeroDivisionError:
    print("b should not be zero")
except IndexError:
    print("IndexError")
except:
    print("Something went wrong")