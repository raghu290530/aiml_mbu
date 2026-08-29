'''Write a class Bike with color attribute
defaulting to 'black'. Read a color,
create an object, and print it.
If empty input, print 'black'.'''
class Bike:
    def __init__(self,color):
        if color == "":
            self.color = "Black"
        else:
            self.color = color
b1 = Bike(input())
print(b1.color)
b2 = Bike("Red")
print(b2.color)