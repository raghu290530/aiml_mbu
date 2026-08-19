'''Write a class Rectangle with length and
breadth and a method area() that returns length * breadth.
a method perimeter() that returns 2*(l+b)
'''

class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l + self.b)
r = Rectangle(int(input()),int(input()))
print("Area =", r.area())
print("Per =",r.perimeter())

