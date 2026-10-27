'''Write a class Shape with area()
returning 0, and a class Square(Shape)
with side and area() returning side*side.'''
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,s):
        self.s = s
    def area(self):
        return self.s * self.s
s = Square(int(input()))
print(s.area())