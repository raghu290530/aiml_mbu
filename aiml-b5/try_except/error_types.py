# print(x) NameError:
# z = 5/0 ZeroDivisionError:
# x = int("hi") ValueError:
# li = [4,3,9]
# print(li[3]) IndexError:
# x = "hi" + 5 TypeError:
try:
    a = int(input())
    b = int(input())
    c = a/b
    print(c)
    # print(d)
    print( c + "hi")
except ValueError:
    print("Enter Integers only")
except ZeroDivisionError:
    print("B should not Zero")
except NameError:
    print("D is not defined")
except:
    print("Something went wrong")