'''W.A.P to create 2 classes
1) class A - > x = 5
2) class B-> y = 10
create saperate objects and print respective
properties values/
'''
class A:
    x = 5
    def printName(self):
        print("My Name is A")

class B(A):
    y = 10

b = B()
print(b.y)
print(b.x)
b.printName()