'''Write a class Rectangle with
length and breadth and a method area()
that returns length * breadth.
peremiter() '''
class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
    def perimeter(self):
        return 2 * (self.l + self.b)

r1 = Rectangle(5,6)
print("Area =",r1.area())
print("Perimeter =",r1.perimeter())